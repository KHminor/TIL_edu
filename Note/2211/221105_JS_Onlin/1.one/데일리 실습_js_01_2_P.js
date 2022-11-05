function palindrome(str) {
    if (str === str.split('').reverse().join('')) {
      console.log(true);
    } else {
      console.log(false);
    }
  }
  
  // 출력
  palindrome('level')
  palindrome('hi') 