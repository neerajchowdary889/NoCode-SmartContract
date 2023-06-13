pragma solidity ^0.8.0;

contract Voting {

    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    struct Voter {
        bool voted;
        uint256 candidateId;
        uint256 weight;
        address delegate;
    }

    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    uint256 public candidatesCount;

    event Voted(address indexed voter, uint256 candidateId);
    event Delegated(address indexed delegator, address indexed delegate);

    constructor() {
        addCandidate("Candidate 1");
        addCandidate("Candidate 2");
    }

    function addCandidate(string memory _name) private {
        candidatesCount++;
        candidates.push(Candidate(candidatesCount, _name, 0));
    }

    function getVotesForCandidates() public view returns (uint256[] memory) {
        uint256[] memory votes = new uint256[](candidatesCount);
        for (uint256 i = 0; i < candidatesCount; i++) {
            votes[i] = candidates[i].voteCount;
        }
        return votes;
    }

    function delegate(address _delegate) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "You have already voted!");
        require(_delegate != msg.sender, "You cannot delegate to yourself!");

        while (voters[_delegate].delegate != address(0)) {
            _delegate = voters[_delegate].delegate;
            require(_delegate != msg.sender, "Cannot create a circular delegation!");
        }

        sender.voted = true;
        sender.delegate = _delegate;

        Voter storage delegateVoter = voters[_delegate];
        if (delegateVoter.voted) {
            candidates[delegateVoter.candidateId - 1].voteCount += sender.weight;
        } else {
            delegateVoter.weight += sender.weight;
        }

        emit Delegated(msg.sender, _delegate);
    }

    function vote(uint256 _candidateId) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "You have already voted!");

        sender.voted = true;
        sender.candidateId = _candidateId;
        candidates[_candidateId - 1].voteCount += sender.weight;

        emit Voted(msg.sender, _candidateId);
    }

    function reweight(address _voter, uint256 _weight) public {
        require(_weight > 0, "Weight must be greater than zero!");

        Voter storage sender = voters[msg.sender];
        require(sender.delegate == address(0), "Delegators cannot reweight!");
        require(!sender.voted, "You have already voted!");

        voters[_voter].weight = _weight;
    }

    function getDelegatedVotes(address _voter) public view returns (uint256) {
        Voter storage delegateVoter = voters[_voter];
        require(delegateVoter.delegate != address(0), "This voter has not delegated their vote!");
        require(_voter != msg.sender, "Cannot query your own delegation!");

        return voters[delegateVoter.delegate].weight;
    }

    function getCandidates() public view returns (Candidate[] memory) {
        return candidates;
    }
}