from flask import Flask, request, redirect, render_template, url_for
from flask_talisman import Talisman

############################################################
# SETUP
############################################################

app = Flask(__name__)


############################################################
# ROUTES
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
    }
]

@app.route('/')
def home():
    """Display the home page."""

    context = {}

    return render_template('pages/home.html', **context)

@app.route('/swe_career_guide')
def swe_career_guide():
    """Display the swe_career_guide page."""

    return render_template('pages/swe_career_guide.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

@app.route('/code_solution/<solution_id>')
def code_solution(solution_id):
    """Display the Code Solution page."""

    context = {}

    for product in solutions:
        if product["_id"] == solution_id:
            context = product
            break

    return render_template('pages/code_solutions/code_solution.html', **context)

@app.route('/search_solutions')
def search_solutions():
    """Display the search_solutions page."""

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
        "solutions": solutions
    }

    return render_template('pages/code_solutions/search_solutions.html', **context)

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=True)