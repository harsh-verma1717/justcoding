// Solidity program to implement
// the above approach
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.21;

contract TestContract 
{
  uint public counter = 0;

  constructor() public 
  {
    IncrementCounter();
  }

  function IncrementCounter() public 
  {
    counter ++;
  }
}

