pragma solidity ^0.5.0;

contract Functions {

	final address owner;

	constructor() public{
	    owner = me;
	}

    function f1(uint@me x) public{
    }

    function f2(uint@all x) public{
    }

    function f3(uint@me abc_def) public{
    }

    function f4(uint x) public{
    }
}

