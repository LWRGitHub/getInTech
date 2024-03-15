from flask import Flask, request, redirect, render_template, url_for
from flask_talisman import Talisman
import os
import time

# forms
from web_forms import SearchForm



############################################################
# SETUP
############################################################



app = Flask(__name__)

# Secret Key for CSRF Protection in Flask-WTF
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

############################################################
# DATA
############################################################


solutions = [
    {
        "name": "3 Sum",
        "site": "LeetCode",
        "_id": "9827643rb27b27v",
        "href": "/solution/9827643rb27b27v",
        "video": {
            "has_video": False,
            "scripts": ["Video1 Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
def threeSum(nums):

    nums.sort()
    res = []

    for i in range(len(nums)):

        if nums[i] > 0:
            break
        elif i == 0 or nums[i-1] != nums[i]:
            sum0(nums, i, res)

    return res

def sum0(nums, i, res):

    sm = i + 1
    lg = len(nums) - 1

    while sm < lg:
        sum = nums[i] + nums[sm] + nums[lg]

        if sum < 0:
            sm+= 1
        elif sum > 0:
            lg-= 1
        else:
            res.append([nums[i], nums[sm], nums[lg]])
            sm+= 1
            lg-= 1
            while(sm < len(nums) and nums[sm] == nums[sm-1]):
                sm+= 1'''
            },
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const threeSum = function(nums, res=[]) {
    nums.sort((a,b) => a - b);
    for(let i = 0; i < nums.length; i++){
        if(nums[i] > 0){
            break;
        } else if(i === 0 || nums[i-1] !== nums[i]){
            sum0(nums, i, res);
        }
    }
    return res;
};

const sum0 = (nums, i, res, sm=i+1, lg=nums.length-1) => {
    while(sm < lg){
        const sum = nums[i] + nums[sm] + nums[lg];
        if(sum < 0){
            sm++;
        } else if(sum > 0) {
            lg--;
        } else {
            res.push([nums[i], nums[sm], nums[lg]]);
            sm++;
            lg--;
            while(nums[sm] === nums[sm-1]){
                sm++;
            }
        }
    }
};'''
            }
        ]
    },
    {
        "name": "Two Sum",
        "site": "LeetCode",
        "_id": "liauwehfipuwefhlkw98237r23",
        "href": "/solution/liauwehfipuwefhlkw98237r23",
        "video": {
            "has_video": False
        },
         "languages": [
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
def twoSum(nums, target):
    memo = {}
    for i in range(len(nums)):

        need = target - nums[i]
        if need in memo:
            return [i, memo[need]]

        memo[nums[i]] = i '''
            },
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const twoSum = function(nums, t, m={}) {
    for(let i = 0; i < nums.length; i++){
        const need = t - nums[i];
        if(need in m ) return [i, m[need]];
        m[nums[i]] = i;
    }
};'''
            },
            {
                "name": "Go",
                "abbreviation_for_prism_styles": "go",
                "code":'''
func twoSum(nums []int, target int) []int {
	memo := make(map[int]int)
	for i, num := range nums {
		if val, is := memo[target-num]; is {
			return []int{i, val}
		}
		memo[num] = i
	}
	return []int{}
}'''
            },
            {
                "name": "Java",
                "abbreviation_for_prism_styles": "java",
                "code":'''
static class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        Map<Integer, Integer> memo = new HashMap<>();
        for (int i = 0; i < nums.length; i++) 
        {
            int need = target - nums[i];
            if (memo.containsKey(need)) 
            {
                return new int[] { memo.get(need), i };
            }
            memo.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}'''
            },
            {
                "name": "Swift",
                "abbreviation_for_prism_styles": "swift",
                "code":'''
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        for (i, num) in nums.enumerated() {
            if let j = dict[target - num] {
                return [j, i]
            }
            dict[num] = i
        }
        return []
    }
}'''
            },
        ]
    },
    {
        "name": "Add Two Numbers",
        "site": "LeetCode",
        "_id": "lknas2387b24897b2",
        "href": "/solution/lknas2387b24897b2",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr, carry = dummy, 0

    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry, val = divmod(val, 10)
        curr.next = ListNode(val)
        curr = curr.next
        
    return dummy.next'''
            },
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
class ListNode{
    constructor(val, next = null){
        this.val = val;
        this.next = next;
    }
}
  

const addTwoNumbers = (l1, l2) =>{
    const addLists = (num1, num2, carry = 0) => {
        if (!num1 && !num2 && !carry) return null;
        const newVal = (num1?.val || 0) + (num2?.val || 0) + carry;
        const nextNode = addLists(num1?.next, num2?.next, Math.floor(newVal / 10));
        return new ListNode(newVal % 10, nextNode);
    }
    return addLists(l1, l2);
};'''
            },
            {
                "name": "Java",
                "abbreviation_for_prism_styles": "java",
                "code":'''
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        int carry = 0;
        while(l1!=null || l2!=null || carry==1){
            int num = carry;
            if(l1!=null){
                num+=l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                num+=l2.val;
                l2 = l2.next;
            }
            carry = num / 10;
            curr.next = new ListNode(num % 10);;
            curr = curr.next;
        }
        return dummy.next;
    }
}'''
            },
            {
                "name": "Go",
                "abbreviation_for_prism_styles": "go",
                "code":'''
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry, dummy := 0, new(ListNode)
	for node := dummy; l1 != nil || l2 != nil || carry > 0; node = node.Next {
		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}
		node.Next = &ListNode{carry % 10, nil}
		carry /= 10
	}
	return dummy.Next
}'''
            }
        ]
    },
    {
        "name": "Add Two Promises",
        "site": "LeetCode",
        "_id": "injr237823b2497824",
        "href": "/solution/injr237823b2497824",
        "video": {
            "has_video": False
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const addTwoPromises = async (promise1, promise2) => await promise1 + await promise2;'''
            }
        ]
    },
    {
        "name": "All Paths From Source to Target",
        "site": "LeetCode",
        "_id": "kj23498234b2498724",
        "href": "/solution/kj23498234b2498724",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const allPathsSourceTarget = (graph) =>{
    
    const target = graph.length - 1;
    let ans = new Set;
    
    const backtrack = (currentNode, path) =>{
        
        if(currentNode === target){
            ans.add(path.slice(0));
            return;
        }
        
        for(let i=0; i<graph[currentNode].length; i++){
            
            const nextNode = graph[currentNode][i];
            path.push(nextNode);
            backtrack(nextNode, path);
            path.pop();
        }
    };
    backtrack(0, [0]);
    
    return Array.from(ans); 
};'''
            }
        ]
    },
    {
        "name": "Array Wrapper",
        "site": "LeetCode",
        "_id": "bkhj23893by234872",
        "href": "/solution/bkhj23893by234872",
        "video": {
            "has_video": False
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const ArrayWrapper = function(nums) {
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((a, b) => a + b, 0);;
}

ArrayWrapper.prototype.toString = function() {
    return `[${this.nums}]`;
}'''
            }
        ]
    },
    {
        "name": "Binary Search Tree to Greater Sum Tree",
        "site": "LeetCode",
        "_id": "bh238713yuv2397213vyu2398h",
        "href": "/solution/bh238713yuv2397213vyu2398h",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const bstToGst = (root) =>{
    let lastN = 0;
    const dfs = (n) =>{
        if(!n) return;
        dfs(n.right);
        n.val += lastN;
        lastN = n.val;
        dfs(n.left);
    };
    dfs(root);
    return root;
};'''
            }
        ]
    },
    {
        "name": "Best Time to Buy and Sell Stock",
        "site": "LeetCode",
        "_id": "bnv872bg82yvf79h2guf892hib",
        "href": "/solution/bnv872bg82yvf79h2guf892hib",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const maxProfit = (prices, prf=0, buy=Infinity, sell=-Infinity) =>{
    for(let p of prices){
        if(p<buy){
            buy = p;
            sell = -Infinity;
        }else if(p>sell){
            sell = p;
            prf = Math.max(sell - buy, prf);
        }
    }
    return prf;
};'''
            }
        ]
    },
    {
        "name": "Coin Change",
        "site": "LeetCode",
        "_id": "ibf37894y78asdgf3q4awef22u3yryvbf723bn",
        "href": "/solution/ibf37894y78asdgf3q4awef22u3yryvbf723bn",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
var coinChange = function(coins, amount) {
    const arr = Array.from({length: amount+1}, ()=> -1)
    arr[0] = 0;
    coins.sort((a,b)=>a-b)
  
    for(const coin of coins){
        for(let i=0; i<amount+1; i++){
            if(i >= coin){
                const i2 = i - coin
                let pos = arr[i2] + 1 > 0? arr[i2] + 1 : -1
                if(pos > -1 && arr[i] > -1){
                    arr[i] = Math.min(arr[i], pos)
                }else{
                    arr[i] = arr[i]>-1 ? arr[i] : pos
                }
              
            }
        }
    }
  
    return arr[amount];
};'''
            }
        ]
    },
    {
        "name": "Compare Version Numbers",
        "site": "LeetCode",
        "_id": "nklgvno934uongn98923uogboub8h989ukvkb",
        "href": "/solution/nklgvno934uongn98923uogboub8h989ukvkb",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const addTwoPromises = async (promise1, promise2) => await promise1 + await promise2;'''
            }
        ]
    },
    {
        "name": "Concatenation of Array",
        "site": "LeetCode",
        "_id": "knjsd8923hbg89723jknalkdjvb2837rbfy482bnv",
        "href": "/solution/knjsd8923hbg89723jknalkdjvb2837rbfy482bnv",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const getConcatenation = (nums) => nums.concat(nums);'''
            },
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums'''
            }
        ]
    },
    {
        "name": "Convert The Temperature",
        "site": "LeetCode",
        "_id": "n823ihbgf9723bgf89723b219b2",
        "href": "/solution/n823ihbgf9723bgf89723b219b2",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const convertTemperature = (celsius) => [celsius+273.15, celsius*9/5+32];'''
            },
            {
                "name": "Python",
                "abbreviation_for_prism_styles": "py",
                "code": '''
class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius+273.15, celsius*9/5+32]'''
            }
        ]
    },
    {
        "name": "Count Complete Tree Nodes",
        "site": "LeetCode",
        "_id": "nv9238gn298nvgqbg6363bvdkslwop39i4756fghbvn",
        "href": "/solution/nv9238gn298nvgqbg6363bvdkslwop39i4756fghbvn",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
var countNodes = function(root) {
    let count = 0;

    const dfs = (n) => {
        if(!n) return;
        dfs(n.left);
        dfs(n.right);
        count++;
    }
    dfs(root);
      
    return count;
};'''
            }
        ]
    },
    {
        "name": "Course Schedule",
        "site": "LeetCode",
        "_id": "nnv38e92784bv29772934bvb297379bvvb",
        "href": "/solution/nnv38e92784bv29772934bvb297379bvvb",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
// create the adjacency list
const buildAdjacencyList = (totalNodes, graph) =>{
    // makes >>> obj = {key: [], ...}
    const adjacencyList = Array.from({length: totalNodes}, () => []);

    // Loop through the graph grabbing the node in the adjacent node
    for(let [node, adjacentNode] of graph){
        // push the node and it's adjacent node into the adjacency list
        adjacencyList[node].push(adjacentNode);
    };

    // return adjacency list
    return adjacencyList;
};

// check for a cycle
const hasCycle = (node, adjacencyList, visited, departedCount) =>{
    // Mark the nude as visited
    visited[node] = true;

    // loop through the node adjacent nodes
    for(const adjacent of adjacencyList[node]){
        if(!visited[adjacent]){ // if not visited
            visited[adjacent] = true; // mark as visited
            // if has cycle return true
            if(hasCycle(adjacent, adjacencyList, visited, departedCount)) return true;
        }else{
            // Else if departed count equals zero return true
            if(departedCount[adjacent] === 0) return true;
        }
    }

    // if you get here we're departing and we can return false as there is no cycle
    departedCount[node]++;
    return false;
};

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish = (numCourses, prerequisites) =>{
    // adjacencyList = {node: [<adjacentNode>, ...], ...}
    const adjacencyList = buildAdjacencyList(numCourses, prerequisites);
    const visited = {};
    // departedCount = {node: 0, ...}
    const departedCount = Array.from({length: numCourses}, () => 0);

    // loop through nodes in adjacency list
    for(let node in adjacencyList){
        if(!visited[node]){ // if not visited and has cycle return false
            if(hasCycle(node, adjacencyList, visited, departedCount)) return false; 
        };     
    }; 

    return true;      
};'''
            }
        ]
    },
    {
        "name": "Course Schedule II",
        "site": "LeetCode",
        "_id": "nfv8923bg298b24362b3f8024u249gbg",
        "href": "/solution/nfv8923bg298b24362b3f8024u249gbg",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const findOrder = (numC, prerequ, adj=Array.from({length:numC},()=>[]), idg=Array.from({length:numC},()=>0),q=[],ans=[]) =>{
    console.log(adj);
    console.log(idg);

    for(const [c,pre] of prerequ){
       adj[pre].push(c);
       idg[c]++;
    }
    for(let i=0; i<idg.length; i++){
        if(idg[i] === 0) q.push(i);
    }
    while(q.length){
        const n = q.shift();
        ans.push(n);
        for(const v of adj[n]){
            idg[v]--;
            if(idg[v] === 0) q.push(v);
        }
    }
    if(ans.length === numC) return ans;
    return [];
};'''
            }
        ]
    },
    {
        "name": "Course Schedule III",
        "site": "LeetCode",
        "_id": "ndv8923bv2978b230823bv23u82389b2427hk",
        "href": "/solution/ndv8923bv2978b230823bv23u82389b2427hk",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const scheduleCourse = (courses) =>{

    courses.sort((a,b)=>a[1]-b[1])
    const maxHeap = new MaxPriorityQueue(); 
    let maxTime = 0;

    for(const [time, endTime] of courses){
        if(time + maxTime <= endTime){
            maxHeap.enqueue(time);
            maxTime += time;
        }else if(maxHeap.front() && maxHeap.front().element > time){
            maxTime += time - maxHeap.dequeue().element
            maxHeap.enqueue(time);
        }
    }

    return maxHeap.size(); 
};'''
            }
        ]
    },
    {
        "name": "Deepest Leaves Sum",
        "site": "LeetCode",
        "_id": "vnqoievbg47gg47b2f39823gb298ub42vb80",
        "href": "/solution/vnqoievbg47gg47b2f39823gb298ub42vb80",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const deepestLeavesSum = (root) =>{
    
    deepthObj = {
        deepest: 0,
        nums: []
    }
    
    const dfs = (n, depth)=>{
        if(!root) return;
        depth++;
        if(n.left !== null) dfs(n.left, depth);
        if(n.right !== null) dfs(n.right, depth);
        if(deepthObj.deepest < depth){
            deepthObj.deepest = depth
            deepthObj.nums = [n.val]
        }else if(deepthObj.deepest === depth){
            deepthObj.nums.push(n.val)
        }
    }
   
    dfs(root, 0);
    
    return deepthObj.nums.reduce((a, b) => a + b, 0);
    
};'''
            }
        ]
    },
    {
        "name": "Defanging an IP Address",
        "site": "LeetCode",
        "_id": "nvui4329248bg29823ubg2980b23h2vfy28973",
        "href": "/solution/nvui4329248bg29823ubg2980b23h2vfy28973",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const defangIPaddr = (address) => address.split('.').join("[.]")'''
            }
        ]
    },
    {
        "name": "Design Parking System",
        "site": "LeetCode",
        "_id": "nvjn2oi389424ghbv94894gvbn12308ivbhy5gy5y75",
        "href": "/solution/nvjn2oi389424ghbv94894gvbn12308ivbhy5gy5y75",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
/* ---------------------- *
 *  Brute force solution: *
 * ---------------------- */
var ParkingSystem = function(big, medium, small){
    this.availableParking = {'1':big,'2':medium,'3':small};
};

ParkingSystem.prototype.addCar = function(carType){
    if(this.availableParking[carType] !== 0){
        this.availableParking[carType]--;
        return true;
    }else{
        return false;
    }
};

/* ------------------- *
 * Optimized solution: *
 * ------------------- */
var ParkingSystem = function(big, medium, small){
    this.availableParking = {'1':big,'2':medium,'3':small};
};

ParkingSystem.prototype.addCar = function(carType){
    return this.availableParking[carType]-- > 0;
};'''
            }
        ]
    },
    {
        "name": "Edit Distance",
        "site": "LeetCode",
        "_id": "nvui4vb2478bf2298bvb2837vr2892nvb387ygh",
        "href": "/solution/nvui4vb2478bf2298bvb2837vr2892nvb387ygh",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const minDistance = (word1, word2)=>{
    const dp = Array(word1.length+1).fill(0).map(()=>Array(word2.length+1).fill(0));
    for(let i = 0; i <= word1.length; i++){
        dp[i][0] = i;
    };
    for(let j = 0; j <= word2.length; j++){
        dp[0][j] = j;
    };
    for(let i = 1; i <= word1.length; i++){
        for(let j = 1; j <= word2.length; j++){
            if(word1[i-1] === word2[j-1]){
                dp[i][j] = dp[i-1][j-1];
            }else{
                dp[i][j] = 1 + Math.min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]);
            };
        };
    };
    return dp[word1.length][word2.length];
};'''
            }
        ]
    },
    {
        "name": "Final Value of Variable After Performing Operations",
        "site": "LeetCode",
        "_id": "vn40g75b209fn2ou3bt08312bt10r18o3tb1o3ubfb",
        "href": "/solution/vn40g75b209fn2ou3bt08312bt10r18o3tb1o3ubfb",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const finalValueAfterOperations = (operations) => {
    let x = 0;
    for(i in operations){
        const o = operations[i]
        if(o === "++X" || o === "X++"){
            x++;
        }else{
            x--;
        } 
    }
    return x;
};'''
            }
        ]
    },
    {
        "name": "Find Center of Star Graph",
        "site": "LeetCode",
        "_id": "nv894bg2987bg9284bg2ou3bfnbdkeytghnr48",
        "href": "/solution/nv894bg2987bg9284bg2ou3bfnbdkeytghnr48",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const findCenter = (e) => e[0][0] === e[1][0] || e[0][0] === e[1][1] ? e[0][0] : e[0][1];'''
            }
        ]
    },
    {
        "name": "Find Median from Data Stream",
        "site": "LeetCode",
        "_id": "vnowgb94782fb293ufhbfg984gub",
        "href": "/solution/vnowgb94782fb293ufhbfg984gub",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const {
    PriorityQueue,
    MinPriorityQueue,
    MaxPriorityQueue,
} = require('@datastructures-js/priority-queue');


var MedianFinder = function() {

    this.maxHeap = new MaxPriorityQueue();
    this.minHeap = new MinPriorityQueue();
    
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    if(this.maxHeap.size() === 0 || num < this.maxHeap.front().element){
        this.maxHeap.enqueue(num);
    }else{
        this.minHeap.enqueue(num);
    };

    if(this.maxHeap.size() - this.minHeap.size() > 1){
        this.minHeap.enqueue(this.maxHeap.dequeue().element);
    }else if(this.minHeap.size() - this.maxHeap.size()> 1){
        this.maxHeap.enqueue(this.minHeap.dequeue().element);
    }
   
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    if(this.maxHeap.size() > this.minHeap.size()){
        return this.maxHeap.front().element;
    }else if(this.minHeap.size() > this.maxHeap.size()){
        return this.minHeap.front().element;
    }else{
        return (this.minHeap.front().element + this.maxHeap.front().element) / 2;
    }
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */'''
            }
        ]
    },
    {
        "name": "Find Mode in Binary Search Tree",
        "site": "LeetCode",
        "_id": "vnieb23948b2i3yfbbfoiug2498bgi2u34hg2u3bnf2io3gn",
        "href": "/solution/vnieb23948b2i3yfbbfoiug2498bgi2u34hg2u3bnf2io3gn",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
var findMode = function(root) {
  const memo = {}

  const dfs = (n) =>{
    if(!n) return;
      
    dfs(n.left);
    dfs(n.right);
    if(n.val in memo){
      memo[n.val]++;
    }else{
      memo[n.val] = 1;
    }
    
  }
    dfs(root)
  const arr = Object.entries(memo).sort((a,b)=> b[1] - a[1]);
  let ans = [];
  
  for(let i=0; i<arr.length; i++){
    if(arr[i][1] === arr[0][1]){
      ans.push(arr[i][0])
    }else{
      break; 
    }
  }
  return ans;
};'''
            }
        ]
    },
    {
        "name": "Find the Index of the First Occurrence in a String",
        "site": "LeetCode",
        "_id": "vnwoengv2497gb1287bemeort9uytb3m2k2v9",
        "href": "/solution/vnwoengv2497gb1287bemeort9uytb3m2k2v9",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "languages": [
            {
                "name": "JavaScript",
                "abbreviation_for_prism_styles": "js",
                "code": '''
const strStr = (haystack, needle) => haystack.indexOf(needle);'''
            }
        ]
    },
]




############################################################
# ROUTES
############################################################


# Home pg
@app.route('/')
def home():
    """Display the home page."""

    context = {}

    return render_template('pages/home.html', **context)


# Carreer Guide pg
@app.route('/swe_career_guide')
def swe_career_guide():
    """Display the swe_career_guide page."""

    return render_template('pages/swe_career_guide.html')


# 404 pg
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


# Code Solutions pg
@app.route('/code_solution/<solution_id>')
def code_solution(solution_id):
    """Display the Code Solution page."""

    context = {}

    for product in solutions:
        if product["_id"] == solution_id:
            context = product
            break

    return render_template('pages/code_solutions/code_solution.html', **context)



# Pass Stuff to Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# Pass Stuff to Navbar
# @app.context_processor
# def search(query):
#     form = SearchForm()
#     form.searched.data = query
#     return dict(form=form)


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    
    """
        TODO: 
            - fix issue with search not working due to validation
            - then Add back in validation here & in base.html 👇👇👇 
                if form.validate_on_submit():
    """

    # if form.validate_on_submit():
    if form.searched.data != None and form.searched.data != "":
       

        # remove extra spaces
        query = " ".join(form.searched.data.strip().split())
        
        
        return redirect(url_for('search_solutions', query=query, page_number=0))
        # 
    else:
        # print('form.searched.data: ',  type(form.searched.data))
        return redirect(url_for('search_solutions', query="None", page_number=0))


# Search res pg
@app.route('/search_solutions/<query>/<page_number>') 
def search_solutions(query, page_number):
    """Display the search_solutions page."""

    form = SearchForm()

    context = {
        "page": {
            "name": "Code Solutions"
        },
        "other_example": [
            {
                "name": "Example",
                "src": "",
                "alt": "img"
            },
        ],
        "form": form
    }

    if query != "None":
        context["searched"] = query
        context["solutions"] = [solution for solution in solutions if query.lower() in solution["name"].lower()]
        # context["solutions"] = [solution for solution in solutions if query.lower() in solution["name"].like('%{query}%')]
        # context["solutions"] = solutions.filter(solutions.name.like(f"%{query}%"))
    else:
        context["searched"] = False
        context["solutions"] = solutions   

    return render_template('pages/code_solutions/search_solutions.html', **context)


# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)