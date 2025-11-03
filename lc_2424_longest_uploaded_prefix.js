/**
 * NOTE: My idea here is basically just to use a hashmap. As elements are added to the list, we update the pointer from video n-1 to point to video n+1. The as videos come in, if it matches our current longest uploaded prefix, we can move to the next one in our dict.
 */

/**
 * @param {number} n
 */

var LUPrefix = function (n) {
  this.head = 1;
  this.linksForward = {};
  this.linksBackward = {};
  for (let i = 0; i < n + 1; i++) {
    this.linksForward[i] = i + 1;
    this.linksBackward[i + 1] = i;
  }
};

/**
 * @param {number} video
 * @return {void}
 */
LUPrefix.prototype.upload = function (video) {
  if (video === this.head) {
    // console.log("Links forward ", this.linksForward);
    this.head = this.linksForward[this.head];
  }
  let prev = this.linksBackward[video];
  let next = this.linksForward[video];
  this.linksBackward[next] = prev;
  this.linksForward[prev] = next;
  // console.log("Links forward after add is", this.linksForward);
  // console.log("Head after adding vid " + video + " is " + this.head);
};

/**
 * @return {number}
 */
LUPrefix.prototype.longest = function () {
  return this.head - 1;
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = new LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */

var obj = new LUPrefix(4);
obj.upload(3);
console.log(obj.longest()); // 0
obj.upload(1);
console.log(obj.longest()); // 1
obj.upload(2);
console.log(obj.longest()); // 3
