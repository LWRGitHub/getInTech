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
        "_id": "LeetCode-3sum",
        "href": "/solution/LeetCode-3sum",
    },
    {
        "name": "Two Sum",
        "site": "LeetCode",
        "_id": "LeetCode-Two-Sum",
        "href": "/solution/LeetCode-Two-Sum",
    },
    {
        "name": "Add Two Numbers",
        "site": "LeetCode",
        "_id": "LeetCode-Add-Two-Numbers",
        "href": "/solution/LeetCode-Add-Two-Numbers",
    },
    {
        "name": "Add Two Promises",
        "site": "LeetCode",
        "_id": "LeetCode-Add-Two-Promises",
        "href": "/solution/LeetCode-Add-Two-Promises",
    },
    {
        "name": "All Paths From Source to Target",
        "site": "LeetCode",
        "_id": "LeetCode-All-Paths-From-Source-to-Target",
        "href": "/solution/LeetCode-All-Paths-From-Source-to-Target",
    },
    {
        "name": "Array Wrapper",
        "site": "LeetCode",
        "_id": "LeetCode-Array-Wrapper",
        "href": "/solution/LeetCode-Array-Wrapper",
    },
    {
        "name": "Binary Search Tree to Greater Sum Tree",
        "site": "LeetCode",
        "_id": "LeetCode-Binary-Search-Tree-to-Greater-Sum-Tree",
        "href": "/solution/LeetCode-Binary-Search-Tree-to-Greater-Sum-Tree",
    },
    {
        "name": "Best Time to Buy and Sell Stock",
        "site": "LeetCode",
        "_id": "LeetCode-Best-Time-to-Buy-and-Sell-Stock",
        "href": "/solution/LeetCode-Best-Time-to-Buy-and-Sell-Stock",
    },
    {
        "name": "Coin Change",
        "site": "LeetCode",
        "_id": "LeetCode-Coin-Change",
        "href": "/solution/LeetCode-Coin-Change",
    },
    {
        "name": "Compare Version Numbers",
        "site": "LeetCode",
        "_id": "LeetCode-Compare-Version-Numbers",
        "href": "/solution/LeetCode-Compare-Version-Numbers",
    },
    {
        "name": "Concatenation of Array",
        "site": "LeetCode",
        "_id": "LeetCode-Concatenation-of-Array",
        "href": "/solution/LeetCode-Concatenation-of-Array",
    },
    {
        "name": "Convert The Temperature",
        "site": "LeetCode",
        "_id": "LeetCode-Convert-The-Temperature",       "href": "/solution/LeetCode-Convert-The-Temperature",
    },
    {
        "name": "Count Complete Tree Nodes",
        "site": "LeetCode",
        "_id": "LeetCode-Count-Complete-Tree-Nodes",
        "href": "/solution/LeetCode-Count-Complete-Tree-Nodes",
    },
    {
        "name": "Course Schedule",
        "site": "LeetCode",
        "_id": "LeetCode-Course-Schedule",
        "href": "/solution/LeetCode-Course-Schedule",
    },
    {
        "name": "Course Schedule II",
        "site": "LeetCode",
        "_id": "LeetCode-Course-Schedule-II",
        "href": "/solution/LeetCode-Course-Schedule-II",
    },
    {
        "name": "Course Schedule III",
        "site": "LeetCode",
        "_id": "LeetCode-Course-Schedule-III",
        "href": "/solution/LeetCode-Course-Schedule-III",
    },
    {
        "name": "Deepest Leaves Sum",
        "site": "LeetCode",
        "_id": "LeetCode-Deepest-Leaves-Sum",
        "href": "/solution/LeetCode-Deepest-Leaves-Sum",
    },
    {
        "name": "Defanging an IP Address",
        "site": "LeetCode",
        "_id": "LeetCode-Defanging-an-IP-Address",
        "href": "/solution/LeetCode-Defanging-an-IP-Address",
    },
    {
        "name": "Design Parking System",
        "site": "LeetCode",
        "_id": "LeetCode-Design-Parking-System",
        "href": "/solution/LeetCode-Design-Parking-System",
    },
    {
        "name": "Edit Distance",
        "site": "LeetCode",
        "_id": "LeetCode-Edit-Distance",
        "href": "/solution/LeetCode-Edit-Distance",
    },
    {
        "name": "Final Value of Variable After Performing Operations",
        "site": "LeetCode",
        "_id": "LeetCode-Final-Value-of-Variable-After-Performing-Operations",
        "href": "/solution/LeetCode-Final-Value-of-Variable-After-Performing-Operations",
    },
    {
        "name": "Find Center of Star Graph",
        "site": "LeetCode",
        "_id": "LeetCode-Find-Center-of-Star-Graph",
        "href": "/solution/LeetCode-Find-Center-of-Star-Graph",
    },
    {
        "name": "Find Median from Data Stream",
        "site": "LeetCode",
        "_id": "LeetCode-Find-Median-from-Data-Stream",
        "href": "/solution/LeetCode-Find-Median-from-Data-Stream",
    },
    {
        "name": "Find Mode in Binary Search Tree",
        "site": "LeetCode",
        "_id": "LeetCode-Find-Mode-in-Binary-Search-Tree",
        "href": "/solution/LeetCode-Find-Mode-in-Binary-Search-Tree",
    },
    {
        "name": "Find the Index of the First Occurrence in a String",
        "site": "LeetCode",
        "_id": "LeetCode-Find-the-Index-of-the-First-Occurrence-in-a-String",
        "href": "/solution/LeetCode-Find-the-Index-of-the-First-Occurrence-in-a-String",
    },
]

solutions_info = [
    {
        "name": "3 Sum",
        "site": "LeetCode",
        "_id": "LeetCode-3sum",
        "href": "/solution/LeetCode-3sum",
        "video": {
            "has_video": False,
            "scripts": ["Video1 Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge is about finding all unique triplets in an array that add up to zero. The solution provided follows a two-step approach: sorting the array and then using a two-pointer technique to find the triplets. Here's a step-by-step explanation along with the corresponding pseudo code:"
            },
            {
                "tag": "h2",
                "content": "1. Sort the Array"
            },
            {
                "tag": "p",
                "content": "First, the array is sorted. This makes it easier to avoid duplicates and to efficiently find the triplets."
            },
            {
                "tag": "code",
                "content": '''
SORT nums'''
            },
            {
                "tag": "h2",
                "content": "2. Iterate through the Array"
            },
            {
                "tag": "p",
                "content": "Next, we iterate through the array, using each element as a potential first element of a triplet. The loop is stopped if the current element is greater than 0 because, given the array is sorted, no three elements can sum to 0 beyond this point."
            },
            {
                "tag": "code",
                "content": '''
FOR i FROM 0 TO length of nums
    IF nums[i] > 0 THEN
        BREAK
    END IF
    IF i == 0 OR nums[i-1] != nums[i] THEN
        findTriplets(nums, i, result)
    END IF
END FOR'''
            },
            {
                "tag": "h2",
                "content": "3. Finding Triplets (Two-Pointer Technique)"
            },
            {
                "tag": "p",
                "content": "For each element nums[i], we use two additional pointers to find pairs that sum up to -nums[i], thus ensuring the total sum is zero. The sm (small) pointer starts just after i, and the lg (large) pointer starts at the end of the array. We move these pointers towards each other until they meet, adjusting them based on the sum of nums[i], nums[sm], and nums[lg]."
            },
            {
                "tag": "code",
                "content": '''
FUNCTION findTriplets(nums, i, result)
    sm = i + 1
    lg = length of nums - 1
    WHILE sm < lg DO
        sum = nums[i] + nums[sm] + nums[lg]
        IF sum < 0 THEN
            sm = sm + 1
        ELSE IF sum > 0 THEN
            lg = lg - 1
        ELSE
            ADD [nums[i], nums[sm], nums[lg]] TO result
            sm = sm + 1
            lg = lg - 1
            WHILE sm < lg AND nums[sm] == nums[sm-1] DO
                sm = sm + 1
            END WHILE
        END IF
    END WHILE
END FUNCTION'''
            },
            {
                "tag": "h2",
                "content": "4. Avoiding Duplicates"
            },
            {
                "tag": "p",
                "content": "To avoid adding duplicate triplets to the result, we skip over any subsequent elements that are equal to the current one. This check is done both at the top-level iteration through nums and after finding a valid triplet, for the sm pointer."
            },
            {
                "tag": "h2",
                "content": "Summary"
            },
            {
                "tag": "p",
                "content": "The algorithm efficiently finds all unique triplets in the array that sum up to zero by first sorting the array, then iterating through it with a fixed first element, and using a two-pointer approach to find complementary pairs for the current element. The careful management of pointers and the conditions for incrementing them ensure that duplicates are avoided."
            },
        ],
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
        ],
        "search_res": {
            "video": {
                "has_video": True,
                "src": [
                    "https://www.youtube.com/embed/jzZsG8n2R9A?si=uwDfaIS98YU3Xb0T",
                    "https://www.youtube.com/embed/cRBSOz49fQk?si=jTOTlZh0rFbZnmPF",
                    "https://www.youtube.com/embed/qJSPYnS35SE?si=uLOE-LePO8NRJa8Q"
                ]
            },
            "languages": [
                {
                    "name": "Python",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "JavaScript",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "TypeScript",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "PHP",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "C-Sharp",
                    "solutions": [
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                },
                {
                    "name": "C-Plus-Plus",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Tutorial Cup",
                            "href": "https://tutorialcup.com/leetcode-solutions/3sum-leetcode-solution.htm"
                        }
                    ],
                },
                {
                    "name": "Java",
                    "solutions": [
                        {
                            "site_name": "Coding Broz",
                            "href": "https://www.codingbroz.com/3sum-leetcode-solution/"
                        },
                        {
                            "site_name": "Tutorial Cup",
                            "href": "https://tutorialcup.com/leetcode-solutions/3sum-leetcode-solution.htm"
                        },
                        {
                            "site_name": "Medium @Norman Aranez",
                            "href": "https://medium.com/@araneznorman/15-3sum-leetcode-31ab6df7969e"
                        }
                    ],
                }
            ]
        },
    },
    {
        "name": "Two Sum",
        "site": "LeetCode",
        "_id": "LeetCode-Two-Sum",
        "href": "/solution/LeetCode-Two-Sum",
        "video": {
            "has_video": False
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves finding two numbers in an array whose sum equals a given target. The solution uses a hash map (or dictionary in Python) to efficiently find the pair. Here's how the solution works along with pseudo code:"
            },
            {
                "tag": "h2",
                "content": "1. Initialize a Hash Map"
            },
            {
                "tag": "p",
                "content": "First, initialize an empty hash map (or dictionary). This will store the array elements as keys and their indices as values."
            },
            {
                "tag": "code",
                "content": '''
Initialize memo as an empty hash map'''
            },
            {
                "tag": "h2",
                "content": "2. Iterate through the Array"
            },
            {
                "tag": "p",
                "content": "Loop through each element in the array. For each element, calculate the complementary value needed to reach the target sum by subtracting the current element's value from the target."
            },
            {
                "tag": "code",
                "content": '''
FOR i FROM 0 TO length of nums - 1
    Set need to target - nums[i]'''
            },
            {
                "tag": "h2",
                "content": "3. Check for Complement in Hash Map"
            },
            {
                "tag": "p",
                "content": "For each element, check if its complement (the 'need' value) already exists in the hash map. If it does, the current element and the element at the index stored in the hash map are the solution."
            },
            {
                "tag": "code",
                "content": '''
Copy code
    IF need EXISTS IN memo
        RETURN [i, memo[need]]'''
            },
            {
                "tag": "h2",
                "content": "4. Store the Current Element in the Hash Map"
            },
            {
                "tag": "p",
                "content": "If the complement isn't found, add the current element and its index to the hash map and proceed. This step is crucial because it records the indices of the elements we've already seen, allowing us to find the complement in constant time."
            },
            {
                "tag": "code",
                "content": '''
    memo[nums[i]] = i
END FOR'''
            },
            {
                "tag": "h2",
                "content": "Pseudo Code Summary"
            },
            {
                "tag": "p",
                "content": "Combining all the steps, we get the following pseudo code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION twoSum(nums, target)
    Initialize memo as an empty hash map

    FOR i FROM 0 TO length of nums - 1
        Set need to target - nums[i]

        IF need EXISTS IN memo
            RETURN [i, memo[need]]

        memo[nums[i]] = i
    END FOR
END FUNCTION'''
            },
            {
                "tag": "h2",
                "content": "Explanation"
            },
            {
                "tag": "p",
                "content": "The key idea of this solution is to use a hash map to keep track of the indices of the elements we've encountered so far. For each element, we check if the complement (the number that, when added to the current element, equals the target) has already been seen. If it has, we immediately return the current index and the index of the complement from the hash map. This approach ensures that the solution runs in linear time, making it efficient even for large arrays."
            },
        ],
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
        "_id": "LeetCode-Add-Two-Numbers",
        "href": "/solution/LeetCode-Add-Two-Numbers",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves adding two non-negative integers represented by two non-empty linked lists, where each node contains a single digit. The digits are stored in reverse order. The goal is to return the sum as a linked list, also in reverse order."
            },
            {
                "tag": "h2",
                "content": "Steps to Solve:"
            },
            {
                "tag": "h5",
                "content": "1. Initialize:"
            },
            {
                "tag": "p",
                "content": "Create a dummy head for the result linked list to simplify adding new nodes. Also, keep a variable for carrying over the value when the sum of two digits is 10 or more."
            },
            {
                "tag": "h5",
                "content": "2. Traverse Both Lists:"
            },
            {
                "tag": "p",
                "content": "Iterate through both linked lists simultaneously, adding corresponding digits and the carry value from the previous addition. If one list is longer than the other, consider the missing digits as 0."
            },
            {
                "tag": "h5",
                "content": "3. Handle Carry Over:"
            },
            {
                "tag": "p",
                "content": "After each sum, if the result is 10 or more, set carry to 1 (to be added in the next node's value), and reduce the sum by 10 (since we only store a single digit per node)."
            },
            {
                "tag": "h5",
                "content": "4. Move to Next Nodes:"
            },
            {
                "tag": "p",
                "content": "Move to the next node in both input linked lists (if available) and the result linked list."
            },
            {
                "tag": "h5",
                "content": "5. Check for Remaining Carry:"
            },
            {
                "tag": "p",
                "content": "After finishing iterating through both lists, if there's still a carry value (meaning the last addition resulted in a value of 10 or more), add a new node with the carry value."
            },
            {
                "tag": "h5",
                "content": "6. Return the Result:"
            },
            {
                "tag": "p",
                "content": "Since the dummy head was used as a starting point, return dummy.next, which points to the head of the resultant linked list."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION addTwoNumbers(l1, l2)
    INITIALIZE dummyNode to a new ListNode()
    INITIALIZE current to dummyNode
    INITIALIZE carry to 0

    WHILE l1 OR l2 OR carry IS NOT 0
        INITIALIZE sum to carry
        IF l1 IS NOT NULL
            ADD l1's value to sum
            MOVE l1 to its next node
        END IF
        IF l2 IS NOT NULL
            ADD l2's value to sum
            MOVE l2 to its next node
        END IF
        
        COMPUTE carry and sum (sum divmod 10)
        current.next = new ListNode with value sum
        MOVE current to its next node

    END WHILE

    RETURN dummyNode.next
END FUNCTION'''
            },
            {
                "tag": "p",
                "content": "This pseudo code outlines the process of iteratively traversing both input linked lists, adding corresponding digits along with any carry from the previous addition, and forming a new linked list to represent the sum. The use of a dummy head node simplifies the process of adding new nodes to the result list."
            },
        ],
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
        "_id": "LeetCode-Add-Two-Promises",
        "href": "/solution/LeetCode-Add-Two-Promises",
        "video": {
            "has_video": False
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves working with JavaScript promises. You're given two promises, promise1 and promise2, both of which resolve to a number. The task is to return a new promise that resolves with the sum of the numbers from promise1 and promise2."
            },
            {
                "tag": "h2",
                "content": "Steps to Solve:"
            },
            {
                "tag": "h5",
                "content": "1. Wait for Promises to Resolve:"
            },  
            {
                "tag": "p",
                "content": "Use the await keyword to wait for each of the two promises to resolve. This allows you to get the resolved value of each promise."
            },
            {
                "tag": "h5",
                "content": "2. Add the Resolved Values:"
            }, 
            {
                "tag": "p",
                "content": "Once you have both resolved values, add them together."
            },
            {
                "tag": "h5",
                "content": "3. Return a Promise:" 
            },
            {
                "tag": "p",
                "content": "Since the function is asynchronous (because of the await keyword), it automatically returns a promise. This promise will resolve with the sum of the two resolved values from promise1 and promise2."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
ASYNC FUNCTION addTwoPromises(promise1, promise2)
    // Wait for the first promise to resolve and store its value
    value1 = AWAIT promise1
    
    // Wait for the second promise to resolve and store its value
    value2 = AWAIT promise2
    
    // Return the sum of the two values
    RETURN value1 + value2
END FUNCTION'''
            },
            {
                "tag": "h2",
                "content": "Explanation:"
            },
            {
                'tag': 'h5',
                'content': 'Async Function:'
            },
            {
                'tag': 'p',
                'content': 'The function is declared with async to allow the use of the await keyword inside it. This also means the function returns a promise.'
            },
            {
                'tag': 'h5',
                'content': 'Awaiting Promises:'
            },
            {
                'tag': 'p',
                'content': 'The await keyword is used to pause the execution of the function until the promise resolves. This makes the asynchronous promise handling appear more synchronous.'
            },
            {
                'tag': 'h5',
                'content': 'Summing Values:'
            },
            {
                'tag': 'p',
                'content': 'After both promises have resolved, their values are added together. The sum is then automatically wrapped in a promise and returned by the async function.'
            },
            {
                'tag': 'p',
                'content': 'This approach simplifies handling asynchronous operations by making the code appear more like synchronous code, improving readability and maintainability.'
            },
        
        ],
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
        "_id": "LeetCode-All-Paths-From-Source-to-Target",
        "href": "/solution/LeetCode-All-Paths-From-Source-to-Target",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": 'p',
                "content": "This coding challenge involves finding all paths from the start node (node 0) to the end node (node n-1) in a Directed Acyclic Graph (DAG). The approach to solve this problem involves using Depth-First Search (DFS) with backtracking."
            },
            {
                "tag": 'h2',
                "content": "Steps to Solve:"
            },
            {
                "tag": 'h5',
                "content": "1. Initialization:"
            },
            {
                "tag": 'p',
                "content": "Define a variable to hold the final result (list of paths). Also, define the target node, which is the last node (n-1)."
            },
            {
                "tag": 'h5',
                "content": "2. Depth-First Search (DFS) Function:"
            },
            # ul
            {
                "tag": 'p',
                "content": "This function, let's call it DFS, will take the current node and the current path as arguments. If the current node is the target node, add the current path to the result and return. If the current node is the target node, add the current path to the result and return. Iterate over all adjacent nodes of the current node. For each adjacent node. Add the adjacent node to the current path. Recursively call DFS with the adjacent node and the updated path. Backtrack by removing the last node added to the path (to explore other paths)."
            },
            {
                "tag": 'h5',
                "content": "3. Backtracking:"
            },
            {
                "tag": 'p',
                "content": "This is implicitly done by the DFS function by adding and then removing nodes from the current path as it explores different paths."
            },
            {
                "tag": 'h5',
                "content": "4. Start DFS: "
            },
            {
                "tag": 'p',
                "content": "Begin the DFS from node 0 with an initial path containing just the start node."
            },
            {
                "tag": 'h5',
                "content": "5. Return Result:"
            },
            {
                "tag": 'p',
                "content": "Convert the result set to an array or list and return it."
            },
            {
                "tag": 'h2',
                "content": "Pseudo Code:"
            },
            {
                'tag': 'code',
                'content': """
FUNCTION allPathsSourceTarget(graph)
    target = LENGTH(graph) - 1
    result = NEW LIST

    FUNCTION DFS(currentNode, path)
        IF currentNode IS target
            ADD path TO result
            RETURN
        END IF

        FOR each nextNode IN graph[currentNode]
            ADD nextNode TO path
            DFS(nextNode, path)
            REMOVE last element from path (BACKTRACK)
        END FOR
    END FUNCTION

    INITIAL_PATH = [0]
    DFS(0, INITIAL_PATH)

    RETURN result
END FUNCTION"""
            },
            {
                'tag': 'p',
                'content': 'In this solution, the DFS function is defined within the allPathsSourceTarget function and recursively explores all paths from the start node to the target node. By adding and removing nodes from the path within the loop, the function effectively backtracks after exploring all paths from a given node, allowing it to explore all possible paths without revisiting the same path.'
            },



        ],
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
        "_id": "LeetCode-Array-Wrapper",
        "href": "/solution/LeetCode-Array-Wrapper",
        "video": {
            "has_video": False
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, you need to create a class ArrayWrapper that encapsulates an array of integers and defines custom behavior for addition and string representation operations. Here's a step-by-step explanation along with pseudo code:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Class Definition"
            },
            {
                "tag": "p",
                "content": "Begin by defining a class named ArrayWrapper. The constructor of the class should accept an array of integers, nums, and store it as an instance variable."
            },
            {
                "tag": "h2",
                "content": "Step 2: Addition Operation"
            },
            {
                "tag": "p",
                "content": "To enable the addition of two ArrayWrapper instances using the + operator, you need to override a method that JavaScript uses internally when addition is performed. In JavaScript, this is typically achieved by defining or overriding the valueOf() method. The valueOf() method should iterate through the array stored in the instance and calculate the sum of its elements. This sum will then be used when the + operator is involved."
            },
            {
                "tag": "h2",
                "content": "Step 3: String Representation"
            },
            {
                "tag": "p",
                "content": "To define how an ArrayWrapper instance is converted to a string, you should override the toString() method. The toString() method should return a string representation of the array, formatted as a comma-separated list of elements enclosed in square brackets [ and ]."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                'tag': 'code',
                'content': """
Class ArrayWrapper
    Constructor(nums)
        this.nums = nums

    Method valueOf()
        sum = 0
        For each num in this.nums
            sum = sum + num
        EndFor
        Return sum

    Method toString()
        Return "[" + this.nums.join(",") + "]"
EndClass"""
            },
            {
                'tag': 'h2',
                'content': 'Usage Examples'
            },
            {
                'tag': 'p',
                'content': 'Creating instances:'
            },
            {
                'tag': 'code',
                'content': """
obj1 = new ArrayWrapper([1, 2])
obj2 = new ArrayWrapper([3, 4])"""
            },
            {
                'tag': 'p',
                'content': 'Adding instances:'
            },
            {
                'tag': 'code',
                'content': """
result = obj1 + obj2  // result would be 10"""
            },
            {
                'tag': 'h2',
                'content': 'Converting to string:'
            },
            {
                'tag': 'code',
                'content': """
strRepresentation = String(obj1)  // strRepresentation would be "[1,2]" """
            },
            {
                'tag': 'p',
                'content': 'This pseudo code outlines the structure and logic needed to meet the requirements of the coding challenge. The actual JavaScript implementation provided does this by defining the ArrayWrapper function as a constructor and adding the valueOf and toString methods to its prototype, allowing all instances to share these methods.'
            },
        ],
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
        "_id": "LeetCode-Binary-Search-Tree-to-Greater-Sum-Tree",
        "href": "/solution/LeetCode-Binary-Search-Tree-to-Greater-Sum-Tree",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, you need to convert a given Binary Search Tree (BST) into a Greater Tree where each node's value is updated to be itself plus the sum of all values greater than it in the BST. The solution involves a depth-first search (DFS) traversal, specifically a reverse in-order traversal (right node, current node, left node), to accumulate the sum of nodes' values in a descending order. Here's how you can solve it along with the pseudo code:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Initialize a Variable"
            },
            {
                "tag": "p",
                "content": "Initialize a variable, say lastSum, to store the cumulative sum of node values encountered during the traversal. Start with lastSum set to 0."
            },
            {
                "tag": "h2",
                "content": "Step 2: Define a Recursive DFS Function"
            },
            {
                "tag": "p",
                "content": "Define a recursive function, say convertToGreaterTree(node), which will perform the reverse in-order traversal and update each node's value."
            },
            {
                "tag": "h2",
                "content": "Step 3: Reverse In-Order Traversal"
            },
            {
                "tag": "p",
                "content": "If the current node (node) is null, return immediately, as there's nothing to process. Recursively call convertToGreaterTree(node.right) to start traversal from the rightmost node (the largest value in a BST). Add lastSum to the current node's value (node.val) and update lastSum to be the new value of node.val. This step ensures that each node's value is updated to include the sum of all greater values in the tree. Recursively call convertToGreaterTree(node.left) to process the left subtree, which contains smaller values."
            },
            {
                "tag": "h2",
                "content": "Step 4: Initiate the Traversal"
            },
            {
                "tag": "p",
                "content": "Call convertToGreaterTree(root) with the root of the BST to start the conversion process."
            },
            {
                "tag": "h2",
                "content": "Step 5: Return the Modified Tree"
            },
            {
                "tag": "p",
                "content": "After the recursive function has updated all nodes, return the root of the modified tree."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                'tag': 'code',
                'content': """
Function bstToGst(root)
    Initialize lastSum to 0

    Function convertToGreaterTree(node)
        If node is null, return

        // Traverse the right subtree
        convertToGreaterTree(node.right)

        // Update the current node's value and lastSum
        node.val = node.val + lastSum
        lastSum = node.val

        // Traverse the left subtree
        convertToGreaterTree(node.left)
    EndFunction

    // Start the conversion from the root
    convertToGreaterTree(root)

    Return root
EndFunction"""
            },
            {
                'tag': 'h2',
                'content': 'Explanation'
            },
            {
                'tag': 'p',
                'content': 'This algorithm leverages the properties of a BST to ensure that when we traverse the tree in reverse in-order order (right subtree, current node, left subtree), we visit nodes in descending order. By maintaining a running sum of all previously visited node values (lastSum), we can update each node to be the sum of its original value and all greater values in the BST. This results in the BST being transformed into a Greater Tree as required by the problem statement.'
            },
        ],
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
        "_id": "LeetCode-Best-Time-to-Buy-and-Sell-Stock",
        "href": "/solution/LeetCode-Best-Time-to-Buy-and-Sell-Stock",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        'how_to': [
            {
                'tag': 'p',
                'content': 'This coding challenge involves finding the maximum profit from a single buy-sell transaction given a list of stock prices over consecutive days. The key idea is to keep track of the minimum purchase price (buy) seen so far and the maximum profit that can be achieved with each new price encountered.'
            },
            {
                'tag': 'h2',
                'content': 'Steps to Solve:'
            },
            {
                'tag': 'h5',
                'content': '1. Initialize Variables:'
            },
            {
                'tag': 'p',
                'content': 'Initialize two variables: profit to track the maximum profit and buy to keep track of the minimum purchase price so far. Set profit to 0 and buy to a very high value (Infinity) to ensure any price will be lower.'
            },
            {
                'tag': 'h5',
                'content': '2. Iterate Through Prices:'
            },
            {
                'tag': 'p',
                'content': 'For each price p in the prices array, perform the following checks and updates:'
            },
            {
                'tag': 'h5',
                'content': '3. Buying Condition:'
            },
            {
                'tag': 'p',
                'content': 'If p is less than buy, update buy to p. Also, reset sell to a very low value (-Infinity) to ensure the next sell price is higher than the new buy price.'
            },
            {
                'tag': 'h5',
                'content': '4. Selling Condition: '
            },
            {
                'tag': 'p',
                'content': 'If p is greater than sell, update sell to p. Update profit to the maximum of the current profit and the difference between sell and buy.'
            },
            {
                'tag': 'h5',
                'content': '5. Return Profit:'
            },
            {
                'tag': 'p',
                'content': 'After iterating through all prices, return the maximum profit achieved.'
            },
            {
                'tag': 'h2',
                'content': 'Pseudo Code'
            },
            {
                'tag': 'code',
                'content': '''
Function maxProfit(prices)
    Initialize profit to 0
    Initialize buy to Infinity
    Initialize sell to -Infinity

    For each price p in prices
        If p < buy
            Update buy to p
            Reset sell to -Infinity
        Else if p > sell
            Update sell to p
            Update profit to max(profit, sell - buy)

    Return profit
EndFunction'''
            },
            {
                'tag': 'h2',
                'content': 'Explanation of Solution'
            },
            {
                'tag': 'p',
                'content': 'The solution effectively scans through the list of prices once (O(n) complexity), updating the buy price whenever a lower price is found. This guarantees buying at the lowest price up to that point. When a higher sell price is encountered, the potential profit (sell - buy) is calculated. If this profit is greater than the current maximum profit, the maximum profit is updated. This approach ensures that the maximum profit possible with a single buy-sell transaction is found, adhering to the constraint that the buy must occur before the sell.'
            },
        ],
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
        "_id": "LeetCode-Coin-Change",
        "href": "/solution/LeetCode-Coin-Change",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, you can use dynamic programming, specifically the bottom-up approach. The problem asks for the fewest number of coins needed to make up a given amount using coins of different denominations. Here's how to approach it:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Initialize"
            },
            {
                "tag": "p",
                "content": "Create an array, let's call it dp, with a length of amount + 1 to store the minimum number of coins needed for each amount from 0 to amount. Initialize this array with a value that indicates an impossible situation, such as -1. Set dp[0] = 0 because the minimum number of coins needed to make up an amount of 0 is 0."
            },
            {
                "tag": "h2",
                "content": "Step 2: Sort Coins"
            },
            {
                "tag": "p",
                "content": "Although not always necessary, sorting the coins can sometimes improve efficiency. This ensures you're always starting with the smallest denomination."
            },
            {
                "tag": "h2",
                "content": "Step 3: Dynamic Programming"
            },
            {
                "tag": "p",
                "content": "Loop through each coin denomination. For each coin, iterate through the dp array starting from the coin's value up to the target amount. For each amount i that is at least as large as the current coin's value, calculate the minimum number of coins needed as follows: Find the previous amount i - coin in the dp array and add 1 to it (since you're using one more coin). Compare this number with the current value in dp[i] (if it's not -1, which means it's been updated before) and take the minimum. Update dp[i] with this minimum number."
            },
            {
                "tag": "h2",
                "content": "Step 4: Return the Result"
            },
            {
                "tag": "p",
                "content": "After filling the dp array, the value at dp[amount] will represent the fewest number of coins needed to make up the amount. If dp[amount] is still -1, it means it's impossible to make up the amount with the given coins, so return -1."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function coinChange(coins, amount)
    Initialize dp array of length amount + 1 with -1
    dp[0] = 0
    
    Sort coins array
    
    For each coin in coins
        For i from coin to amount
            If i >= coin
                If dp[i - coin] is not -1
                    If dp[i] is -1
                        dp[i] = dp[i - coin] + 1
                    Else
                        dp[i] = Min(dp[i], dp[i - coin] + 1)
    
    Return dp[amount]
End Function'''
            },
            {
                "tag": "p",
                "content": "This pseudo code outlines the dynamic programming approach to solving the problem by iteratively building up the solution for all amounts from 1 to amount using the given coin denominations."
            },
        ],
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
        "_id": "LeetCode-Compare-Version-Numbers",
        "href": "/solution/LeetCode-Compare-Version-Numbers",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "The provided solution does not match the problem statement. The solution seems to be for adding two promises, which is unrelated to comparing version numbers. For the problem of comparing two version numbers, the correct approach involves parsing and comparing the numbers part by part. Here's how to approach it:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Split the Version Numbers"
            },
            {
                "tag": "p",
                "content": "Split both version1 and version2 by the dot '.' to separate the revisions into arrays."
            },
            {
                "tag": "h2",
                "content": "Step 2: Compare Revisions"
            },
            {
                "tag": "p",
                "content": "Iterate over the revisions, comparing the integer values of the corresponding elements from each version. Since one version might have more revisions than the other, continue comparing with 0 if one version runs out of revisions."
            },
            {
                "tag": "h2",
                "content": "Step 3: Determine the Result"
            },
            {
                "tag": "p",
                "content": "During each comparison, if a difference is found, return -1 if version1 is less than version2, or 1 if version1 is greater than version2. If the loop completes without finding any differences, it means the versions are equal, so return 0."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function compareVersion(version1, version2)
    v1 = version1.split('.')
    v2 = version2.split('.')
    
    maxLen = Max(length of v1, length of v2)
    
    For i from 0 to maxLen-1
        rev1 = i < length of v1 ? Integer(v1[i]) : 0
        rev2 = i < length of v2 ? Integer(v2[i]) : 0
        
        If rev1 < rev2
            Return -1
        Else if rev1 > rev2
            Return 1
    
    Return 0
End Function'''
            },
            {
                "tag": "p",
                "content": "This pseudo code provides a clear outline of the steps needed to compare the version numbers according to the rules specified in the problem statement."
            },
        ],
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
        "_id": "LeetCode-Concatenation-of-Array",
        "href": "/solution/LeetCode-Concatenation-of-Array",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, you need to create a new array that consists of the original array nums followed by a duplicate of itself. This is straightforward and involves concatenating the original array with a copy of itself. Here's a step-by-step guide and the corresponding pseudo code:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Concatenation"
            },
            {
                "tag": "p",
                "content": "You need to concatenate the original array nums with another instance of itself. There are various ways to do this depending on the programming language being used. In some languages, there might be a built-in function or method for array concatenation."
            },

            {
                "tag": "h2",
                "content": "Step 2: Return the New Array"
            },
            {
                "tag": "p",
                "content": "After concatenating, you will have a new array of length 2n, where n is the length of the original array. This new array is what the problem statement refers to as ans."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
Function getConcatenation(nums)
    // Create a new array 'ans' by concatenating 'nums' with itself
    ans = nums + nums

    // Return the new array
    Return ans
End Function'''
            },
            {
                "tag": "p",
                "content": "This pseudo code uses a simple operation + to represent the concatenation process, assuming the programming environment supports such an operation for arrays. The actual implementation might use a different method or function for concatenation, such as concat() in JavaScript, as shown in the provided solution."
            },
            {
                "tag": "p",
                "content": "The provided solution in JavaScript uses the .concat() method, which joins two or more arrays by returning a new array. In this case, nums.concat(nums) creates a new array by concatenating nums with itself, effectively doubling the array while preserving the order of elements."
            }
        ],
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
        "_id": "LeetCode-Convert-The-Temperature",       "href": "/solution/LeetCode-Convert-The-Temperature",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, you'll need to perform two straightforward calculations to convert a temperature from Celsius to Kelvin and Fahrenheit. The given formulas are:"
            },
            {
                "tag": "h5",
                "content": "Kelvin = Celsius + 273.15"
            },
            {
                "tag": "h5",
                "content": "Fahrenheit = Celsius * 1.80 + 32.00"
            },
            {
                "tag": "p",
                "content": "Using these formulas, you can easily write a function that takes celsius as its input and returns an array containing the converted temperatures in Kelvin and Fahrenheit."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function convertTemperature(celsius)
    // Initialize an empty array 'ans'
    Initialize ans = []

    // Convert Celsius to Kelvin and add to 'ans'
    kelvin = celsius + 273.15
    Add kelvin to ans

    // Convert Celsius to Fahrenheit and add to 'ans'
    fahrenheit = celsius * 1.80 + 32.00
    Add fahrenheit to ans

    // Return the 'ans' array
    Return ans
End Function'''
            },
            {
                "tag": "h2",
                "content": "Explanation"
            },
            {
                "tag": "h5",
                "content": "Kelvin Conversion:"
            },
            {
                "tag": "p",
                "content": "You add 273.15 to the Celsius value to convert it to Kelvin and store this value in the first element of the answer array."
            },
            {
                "tag": "h5",
                "content": "Fahrenheit Conversion:"
            },
            {
                "tag": "p",
                "content": "You multiply the Celsius value by 1.80 and add 32.00 to convert it to Fahrenheit, then store this value as the second element of the answer array."
            },
            {
                "tag": "p",
                "content": "Finally, you return the array containing both converted temperatures."
            },
            {
                "tag": "p",
                "content": "This approach ensures the conversion is accurate to two decimal places as specified, assuming the arithmetic operations in the programming environment adhere to the typical rules of floating-point arithmetic."
            },
        ],
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
        "_id": "LeetCode-Count-Complete-Tree-Nodes",
        "href": "/solution/LeetCode-Count-Complete-Tree-Nodes",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to":[
            {
                "tag": "p",
                "content": "To solve this coding challenge efficiently, especially with the constraint to run in less than O(n) time complexity, you need to leverage the properties of a complete binary tree. The straightforward depth-first search (DFS) solution provided in the example counts all nodes one by one, which leads to O(n) time complexity. However, for a complete binary tree, you can do better by checking the depth of the leftmost and rightmost paths."
            },
            {
                "tag": "h2",
                "content": "Properties of a Complete Binary Tree"
            },
            {
                "tag": "ul",
                "content": ["All levels are fully filled except possibly the last one.","All nodes in the last level are as far left as possible."]
            },
            {
                "tag": "h2",
                "content": "These properties allow us to use the following approach:"
            },
            {
                "tag": "ol",
                "content": [
                    "Calculate the depth of the leftmost path (let's call it leftDepth).",
                    "Calculate the depth of the rightmost path (let's call it rightDepth).",
                    "If leftDepth equals rightDepth, it means the tree is a perfect binary tree, and the total number of nodes can be found by the formula 2^depth - 1, where depth is the depth of the tree.",
                    "If leftDepth does not equal rightDepth, the tree is not perfect, and you need to recursively apply the same procedure to the left and right subtrees and add 1 for the root node."
                ]
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function countNodes(root)
    If root is NULL
        Return 0

    Initialize leftDepth = 0
    Node temp = root
    While temp is not NULL
        Increment leftDepth
        Move temp to temp's left child

    Initialize rightDepth = 0
    temp = root
    While temp is not NULL
        Increment rightDepth
        Move temp to temp's right child

    If leftDepth equals rightDepth
        Return 2^leftDepth - 1

    Else
        Return 1 + countNodes(root.left) + countNodes(root.right)
End Function'''
            },
            {
                "tag": "h2",
                "content": "Explanation"
            },
            {
                "tag": "h5",
                "content": "Base Case:"
            },
            {
                "tag": "p",
                "content": "If the root is NULL, return 0."
            },
            {
                "tag": "h5",
                "content": "Perfect Binary Tree Check:"
            },
            {
                "tag": "p",
                "content": "Calculate the depth of the leftmost and rightmost paths from the root. If they are equal, the tree is perfect, and you can directly return the total node count using the formula 2^depth - 1."
            },
            {
                "tag": "h5",
                "content": "Recursive Case:"
            },
            {
                "tag": "p",
                "content": "If the tree is not perfect, recursively count the nodes in the left and right subtrees and add 1 for the root node."
            },
            {
                "tag": "p",
                "content": "This approach ensures that the algorithm runs faster than O(n) in cases where the tree leverages the properties of a complete binary tree, especially when the tree is nearly perfect, thus reducing the number of recursive calls significantly."
            },
        ],
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
        "_id": "LeetCode-Course-Schedule",
        "href": "/solution/LeetCode-Course-Schedule",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "The provided solution does not directly address the stated problem of counting nodes in a complete binary tree with optimized time complexity. Instead, it seems to be focused on detecting cycles in a graph, which is unrelated to the original task."
            },
            {
                "tag": "p",
                "content": "To solve the original problem of counting the number of nodes in a complete binary tree in less than O(n) time complexity, you can leverage the properties of a complete binary tree. Here's how to approach it:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Calculate Tree Height"
            },
            {
                "tag": "p",
                "content": "Compute the height of the leftmost path (left height) and the rightmost path (right height) from the root. In a complete binary tree, if these heights are equal, it means the tree is a perfect binary tree and you can directly calculate the number of nodes using the formula 2^height - 1."
            },
            {
                "tag": "h2",
                "content": "Step 2: Recursive Split"
            },
            {
                "tag": "p", 
                "content": "If the heights are not equal, recursively apply the same process to the left and right subtrees. The idea is that at least one of the subtrees will be a perfect binary tree, allowing you to avoid traversing all nodes."
            },
            {
                "tag": "h2",
                "content": "Step 3: Combine Counts"
            },
            {
                "tag": "p",
                "content": "Add the counts from the left and right subtrees and include the root node to get the total count for the subtree."
            },  
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function countNodes(root)
    If root is null
        Return 0

    Initialize leftHeight = 0, rightHeight = 0
    Initialize leftNode = root, rightNode = root

    // Calculate the height of the leftmost and rightmost paths
    While leftNode is not null
        Increment leftHeight
        leftNode = leftNode.left

    While rightNode is not null
        Increment rightHeight
        rightNode = rightNode.right

    // If the heights are equal, it's a perfect binary tree
    If leftHeight == rightHeight
        Return 2^leftHeight - 1

    // If not, recursively count nodes in left and right subtrees
    Return 1 + countNodes(root.left) + countNodes(root.right)
End Function'''
            },

            {
                "tag": "h2",
                "content": "Explanation"
            },
            {
                "tag": "h5",
                "content": "Perfect Binary Tree Check:"
            },
            {
                "tag": "p",
                "content": "If the left and right heights are equal, the tree is perfect, and you can calculate the number of nodes directly."
            },
            {
                "tag": "h5",
                "content": "Recursive Count:"
            },
            {
                "tag": "p",
                "content": "If the tree is not perfect, recursively count the nodes in the left and right subtrees and add them together, along with the root node."
            },
            {
                "tag": "p",
                "content": "This approach significantly reduces the time complexity in many cases because it avoids traversing every node in the tree, especially when dealing with perfect binary tree sections."
            },
        ],
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
        "_id": "LeetCode-Course-Schedule-II",
        "href": "/solution/LeetCode-Course-Schedule-II",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves finding a possible order to take all courses given the prerequisites for each course. This problem can be solved using the concept of Topological Sorting in a Directed Graph, where courses are represented as nodes, and prerequisites are represented as directed edges from one node to another. Here's a step-by-step guide and pseudo code for solving this problem:"
            },
            {
                "tag": "h2",
                "content": "Step 1: Graph Representation"
            },
            {
                "tag": "p",
                "content": "Create an adjacency list to represent the directed graph, where the key is a course, and the value is a list of courses that depend on this course (i.e., the courses that can be taken after completing the key course). Create an array to store the in-degree of each node (course). In-degree is the number of incoming edges to a node."
            },
            {
                "tag": "h2",
                "content": "Step 2: Populate Graph and In-Degree Array"
            },
            {
                "tag": "p",
                "content": "Iterate through the prerequisites array. For each pair [a, b] in prerequisites, add a to the adjacency list of b, and increment the in-degree of a by 1."
            },
            {
                "tag": "h2",
                "content": "Step 3: Find Courses with No Prerequisites"
            },
            {
                "tag": "p",
                "content": "Initialize a queue and an array to store the course order. Enqueue all courses with an in-degree of 0 (i.e., courses with no prerequisites)."
            },
            {
                "tag": "h2",
                "content": "Step 4: Process the Queue"
            },
            {
                "tag": "h5",
                "content": "While the queue is not empty:"
            },
            {
                "tag": "ul",
                "content": [
                    "Dequeue a course and add it to the course order array.",
                    "Iterate over its adjacent courses (i.e., courses that can be taken after completing the dequeued course). For each adjacent course, reduce its in-degree by 1. If the in-degree of an adjacent course becomes 0, enqueue it."
                ]
            },
            {
                "tag": "h2",
                "content": "Step 5: Check if All Courses are Processed"
            },
            {
                "tag": "p",
                "content": "After processing the queue, if the course order array contains all the courses (i.e., its length equals numCourses), return the course order array. If not all courses are processed, return an empty array, indicating that it's impossible to complete all courses due to cyclic dependencies or other issues."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code"
            },
            {
                "tag": "code",
                "content": '''
Function findOrder(numCourses, prerequisites)
    Initialize adjacency list and in-degree array
    For each pair [course, prerequisite] in prerequisites
        Add course to adjacency list of prerequisite
        Increment in-degree of course

    Initialize queue and course order array
    For each course
        If in-degree of course is 0
            Enqueue course

    While queue is not empty
        Dequeue a course
        Add it to course order array
        For each adjacent course of dequeued course
            Decrement in-degree of adjacent course
            If in-degree of adjacent course is 0
                Enqueue adjacent course

    If length of course order array equals numCourses
        Return course order array
    Else
        Return empty array
End Function'''
            },
            {
                "tag": "p",
                "content": "This pseudo code outlines the steps to find the order of courses to take, ensuring that prerequisites are met. The algorithm uses a topological sorting approach to process courses in a valid order, respecting all prerequisites."
            },
        ],
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
        "_id": "LeetCode-Course-Schedule-III",
        "href": "/solution/LeetCode-Course-Schedule-III",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                'tag': 'p',
                'content': "To solve this coding challenge, you can use a greedy algorithm approach combined with the use of a max heap (priority queue). The goal is to maximize the number of courses one can take given the constraints of course duration and latest finish day. Here's how the solution works and the corresponding pseudo code:"
            },
            {
                'tag': 'h2',
                'content': 'Solution Explanation:'
            },
            {
                'tag': 'h5',
                'content': '1. Sort Courses:'
            },
            {
                'tag': 'p',
                'content': "First, the courses are sorted based on their lastDay. This is done so that courses with earlier end dates are considered first, aligning with the strategy of minimizing the risk of exceeding course deadlines."
            },
            {
                'tag': 'h5',
                'content': '2. Use Max Heap (Priority Queue):'
            },
            {
                'tag': 'p',
                'content': "A max heap is used to keep track of the courses taken. In this context, the heap stores the durations of the courses. The max heap is helpful because it allows easy access to the course with the longest duration taken so far, which is the first candidate to be dropped if necessary."
            },
            {
                'tag': 'h5',
                'content': '3. Iterate and Decide: '
            },
            {
                'tag': 'p',
                'content': "Iterate through each course. For each course, there are two main decisions:"
            },
            {
                'tag': 'ul',
                'content': [
                    "If the course can be taken within its deadline considering the total duration of courses taken so far (maxTime), add it to the heap and update maxTime.",
                    "If the course cannot be taken by its deadline, check if there's a course that has been taken with a longer duration than the current one (the top of the max heap). If so, replace that course with the current one by removing the longest course from the heap and adding the current course. This is done because replacing a longer course with a shorter one may allow for more courses to be taken."
                ]
            },
            {
                'tag': 'h5',
                'content': '4. Return Result: '
            },
            {
                'tag': 'p',
                'content': "The size of the heap at the end of the iteration represents the maximum number of courses that can be taken, as it contains all the courses that have been successfully scheduled."
            },
            {
                'tag': 'h2',
                'content': 'Pseudo Code:'
            },
            {
                'tag': 'code',
                'content': '''
function scheduleCourse(courses):
    # Sort courses by their end time
    sort courses by lastDay

    # Initialize a max heap and a variable for tracking total time
    maxHeap = new MaxHeap()
    maxTime = 0

    # Iterate through each course
    for each course in courses:
        time, endTime = course

        # If course can be taken within its deadline
        if time + maxTime <= endTime:
            add time to maxHeap
            maxTime += time
        # If not within deadline, but a longer course exists in the heap
        else if maxHeap is not empty and maxHeap.top() > time:
            maxTime += time - maxHeap.pop()
            add time to maxHeap

    # Return the number of courses in the heap
    return size of maxHeap'''
            },
            {
                'tag': 'p',
                'content': "This approach ensures that you always prioritize taking courses that have the earliest deadlines, while also being flexible enough to replace longer-duration courses with shorter ones if it allows for a more optimal schedule."
            }
        ],
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
        "_id": "LeetCode-Deepest-Leaves-Sum",
        "href": "/solution/LeetCode-Deepest-Leaves-Sum",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this challenge, you need to find the sum of the values of the deepest leaves in a binary tree. This involves two main tasks: identifying the deepest leaves and calculating their sum. A depth-first search (DFS) can be used to traverse the tree, track the depth of each leaf, and sum the values of the deepest leaves."
            },
            {
                "tag": "h2",
                "content": "Steps to Solve:"
            },
            {
                "tag": "h5",
                "content": "1. Initialize Depth and Sum Tracking:"
            },
            {
                "tag": "p",
                "content": "Create a structure or object to keep track of the current maximum depth found and the sum of the values of the leaves at that depth."
            },
            {
                "tag": "h5",
                "content": "2. Depth-First Search (DFS) Function:"
            },
            {
                "tag": "p",
                "content": "Implement a DFS function that traverses the tree. This function should take the current node and its depth as parameters."
            },
            {
                "tag": "h5",
                "content": "3. Traverse the Tree:"
            },
            {
                "tag": "p",
                "content": "If the current node is null, return immediately (base case for recursion). Increment the depth as you go deeper into the tree. If the current node is a leaf (no left or right child), compare its depth with the maximum depth found so far:"
            },
            {
                "tag": "ul",
                "content": [
                    "If the depth is greater, update the maximum depth and reset the sum to the current node's value.",
                    "If the depth is equal to the maximum depth, add the current node's value to the sum."
                ]
            },
            {
                "tag": "p",
                "content": "Recursively call the DFS function for the left and right children of the current node."
            },
            {
                "tag": "h5",    
                "content": "4. Start DFS:"
            },
            {
                "tag": "p",
                "content": "Begin the DFS from the root node, starting at depth 0."
            },
            {
                "tag": "h5",
                "content": "5. Return the Sum:"
            },
            {
                "tag": "p",
                "content": "After completing the DFS traversal, return the sum of the deepest leaves."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION deepestLeavesSum(root)
    deepestDepth = 0
    sumOfDeepestLeaves = 0

    FUNCTION DFS(node, depth)
        IF node IS NULL
            RETURN
        END IF

        IF node IS A LEAF
            IF depth > deepestDepth
                deepestDepth = depth
                sumOfDeepestLeaves = node.value
            ELSE IF depth == deepestDepth
                sumOfDeepestLeaves += node.value
            END IF
        END IF

        DFS(node.left, depth + 1)
        DFS(node.right, depth + 1)
    END FUNCTION

    DFS(root, 0)
    RETURN sumOfDeepestLeaves
END FUNCTION'''
            },
            {
                "tag": "p",
                "content": "This pseudo code outlines the steps to find the sum of the values of the deepest leaves in a binary tree using a depth-first search (DFS) approach. This approach ensures that you only keep track of the leaves at the maximum depth and sum their values, fulfilling the challenge's requirements."
            }
        ],
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
        "_id": "LeetCode-Defanging-an-IP-Address",
        "href": "/solution/LeetCode-Defanging-an-IP-Address",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, the goal is to transform a given valid IPv4 address into a 'defanged' version, where every period (.) is replaced with '[.]'. This can be easily achieved by splitting the input string at each period and then joining the resulting array of strings with the defanged period '[.]'."
            },
            {
                "tag": "h2",
                "content": "Steps to Solve:"
            },
            {
                "tag": "h5",
                "content": "1. Split the IP Address:"
            },
            {
                "tag": "p",
                "content": "Split the input IP address string at each period (.), which will create an array of strings, each representing an octet of the IP address."
            },
            {
                "tag": "h5",
                "content": "2. Join with Defanged Period:"
            },
            {
                "tag": "p",
                "content": "Join the array of octet strings using the defanged period '[.]' as the separator."

            },
            {
                "tag": "h5",
                "content": "3. Return the Result:"
            },
            {
                "tag": "p",
                "content": "The result of the join operation is the defanged IP address."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION defangIPaddr(address)
    // Split the address at each period and join with "[.]"
    RETURN address.SPLIT('.').JOIN("[.]")
END FUNCTION'''
            },
            {
                "tag": "h2",
                "content": "Explanation:"
            },
            {
                "tag": "h5",
                "content": "Split:"
            },
            {
                "tag": "p",
                "content": "The SPLIT('.') method divides the IP address into its constituent octets by using the period as a delimiter, resulting in an array of strings."
            },
            {
                "tag": "h5",
                "content": "Join:"
            },
            {
                "tag": "p",
                "content": "The JOIN('[.]') method then assembles these strings back into a single string, inserting '[.]' between each octet, effectively replacing each period in the original IP address."
            },
            {
                "tag": "p",
                "content": "This approach provides a simple and efficient way to create a defanged version of an IPv4 address."
            }
        ],
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
        "_id": "LeetCode-Design-Parking-System",
        "href": "/solution/LeetCode-Design-Parking-System",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, we need to design a ParkingSystem class that manages parking spaces of different sizes. The class should have two main components:"
            },
            {
                "tag": "h5",
                "content": "1. Constructor (ParkingSystem):"
            },
            {
                "tag": "p",
                "content": "Initializes the parking system with a fixed number of slots for each size: big, medium, and small."
            },
            {
                "tag": "h5",
                "content": "2. Method (addCar):"
            },
            {
                "tag": "p",
                "content": "Attempts to park a car of a given type into a slot of its corresponding size. If successful (a slot is available), it decrements the available slot count for that size and returns true. If no slot is available, it returns false."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code for the Solution:"
            },
            {
                "tag": "code",
                "content": '''
CLASS ParkingSystem
    FUNCTION Constructor(big, medium, small)
        // Initialize the available slots for each car type in a map or object
        this.availableParking = {
            '1': big,    // Big car slots
            '2': medium, // Medium car slots
            '3': small   // Small car slots
        }
    END FUNCTION

    FUNCTION addCar(carType)
        // Check if there's an available slot for the given car type
        IF this.availableParking[carType] > 0 THEN
            // Decrement the slot count for that car type and return true
            this.availableParking[carType] = this.availableParking[carType] - 1
            RETURN true
        ELSE
            // Return false if no slot is available
            RETURN false
        END IF
    END FUNCTION
END CLASS'''
            },
            {
                "tag": "h2",
                "content": "Explanation:"
            },
            {
                "tag": "h5",
                "content": "Initialization: "
            },
            {
                "tag": "p",
                "content": "In the Constructor, the ParkingSystem is initialized with the given number of slots for each car type. This information is stored in a key-value pair structure (this.availableParking), where keys are car types (1, 2, and 3 for big, medium, and small, respectively) and values are the counts of available slots."
            },
            {
                "tag": "h5",
                "content": "Adding a Car: "
            },
            {
                "tag": "p",
                "content": "The addCar method checks if there's at least one slot available for the specified car type. If so, it decrements the count of available slots for that car type in this.availableParking and returns true to indicate the car was successfully parked. If there are no available slots for the car type, it returns false."
            },
            {
                "tag": "p",
                "content": "This design allows the ParkingSystem to efficiently manage parking slots and handle parking requests, adhering to the constraints provided in the challenge."
            }
        ],
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
        "_id": "LeetCode-Edit-Distance",
        "href": "/solution/LeetCode-Edit-Distance",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves finding the minimum number of operations required to convert one string (word1) into another (word2). The allowed operations are inserting, deleting, or replacing a character. The problem is a classic example of dynamic programming, specifically the Edit Distance problem (also known as the Levenshtein distance problem)."
            },
            {
                "tag": "h2",
                "content": "Dynamic Programming Approach:"
            },
            {
                "tag": "h5",
                "content": "1. Initialization:"
            },
            {
                "tag": "p",
                "content": "Create a 2D array dp where dp[i][j] represents the minimum number of operations required to convert the first i characters of word1 to the first j characters of word2."
            },
            {
                "tag": "h5",
                "content": "2. Base Cases:"
            },
            {
                "tag": "p",
                "content": "If word1 is empty (i = 0), dp[0][j] is j because it takes j insertions to convert an empty string to the first j characters of word2. If word2 is empty (j = 0), dp[i][0] is i because it takes i deletions to convert the first i characters of word1 to an empty string."
            },
            {
                "tag": "h5",
                "content": "3. Filling the DP Table:"
            },
            {
                "tag": "p",
                "content": "For each pair of indices i and j, compute dp[i][j] as follows:"
            },
            {
                "tag": "p",
                "content": "If the characters word1[i - 1] and word2[j - 1] are the same, no operation is needed for the i-th and j-th characters, so dp[i][j] = dp[i-1][j-1]. If the characters are different, consider the minimum of the following three operations:"
            },
            {
                "tag": "ul",
                "content": [
                    "Inserting (dp[i][j-1] + 1)",
                    "Deleting (dp[i-1][j] + 1)",
                    "Replacing (dp[i-1][j-1] + 1)"
                ]
            },
            {
                "tag": "p",
                "content": "Take the minimum of these three values as dp[i][j]."
            },
            {
                "tag": "h5",
                "content": "4. Return the Result:"
            },
            {
                "tag": "p",
                "content": "The value at dp[word1.length][word2.length] gives the minimum number of operations required."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION minDistance(word1, word2)
    INITIALIZE dp with dimensions [word1.length+1][word2.length+1]

    // Base cases
    FOR i FROM 0 TO word1.length
        dp[i][0] = i
    END FOR
    FOR j FROM 0 TO word2.length
        dp[0][j] = j
    END FOR

    // Fill dp table
    FOR i FROM 1 TO word1.length
        FOR j FROM 1 TO word2.length
            IF word1[i-1] EQUALS word2[j-1]
                dp[i][j] = dp[i-1][j-1]
            ELSE
                dp[i][j] = 1 + MIN(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
            END IF
        END FOR
    END FOR

    RETURN dp[word1.length][word2.length]
END FUNCTION'''
            },
            {
                "tag": "p",
                "content": "This approach efficiently computes the minimum number of operations by building up solutions from smaller subproblems, a hallmark of dynamic programming."
            }
        ],
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
        "_id": "LeetCode-Final-Value-of-Variable-After-Performing-Operations",
        "href": "/solution/LeetCode-Final-Value-of-Variable-After-Performing-Operations",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "This coding challenge involves simulating the effect of a series of operations on a variable X. The operations can be of four types: ++X, X++, --X, and X--. The goal is to determine the final value of X after applying all the operations in the given array."
            },
            {
                "tag": "h2",
                "content": "Steps to Solve:"
            },
            {
                "tag": "h5",
                "content": "1. Initialize Variable X:"
            },
            {
                "tag": "p",
                "content": "Start with X set to 0."
            },
            {
                "tag": "h5",
                "content": "2. Iterate Through Operations:"
            },
            {
                "tag": "p",
                "content": "Go through each operation in the operations array."
            },
            {
                "tag": "h5",
                "content": "3. Determine Operation Type:"
            },
            {
                "tag": "ul",
                "content": ["If the operation is ++X or X++, increment X by 1."," If the operation is --X or X--, decrement X by 1."]
            },
            {
                "tag": "h5",
                "content": "4. Return Final Value:"
            },
            {
                "tag": "p",
                "content": "After all operations are performed, return the final value of X."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION finalValueAfterOperations(operations)
    INITIALIZE X to 0

    FOR EACH operation IN operations
        IF operation EQUALS "++X" OR operation EQUALS "X++" THEN
            INCREMENT X by 1
        ELSE
            DECREMENT X by 1
        END IF
    END FOR

    RETURN X
END FUNCTION'''
            },
            {
                'tag': 'h2',
                'content': 'Explanation:'
            },
            {
                'tag': 'ul',
                'content': ['The for loop iterates through each operation in the given array.',' Inside the loop, a simple if-else conditional checks whether the current operation is an increment operation (++X or X++) or a decrement operation (--X or X--). The value of X is adjusted accordingly.',' After all operations have been applied, the function returns the final value of X. This solution is straightforward and efficient, directly translating the problem statement into code logic.']
            }
        ],
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
        "_id": "LeetCode-Find-Center-of-Star-Graph",
        "href": "/solution/LeetCode-Find-Center-of-Star-Graph",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                'tag': 'p',
                'content': 'To solve this coding challenge, you need to identify the center of a star graph. A star graph has one central node that is connected to all other nodes. Given that the input is a set of edges in a 2D array, where each edge connects two nodes, the central node will be the one that appears in every edge.'
            },
            {
                'tag': 'p',
                'content': "Since the graph is a star graph, examining any two edges is sufficient to determine the center. The center node will be the common node in the first two edges."
            },
            {
                'tag': 'h2',
                'content': 'Steps to Solve:'
            },
            {
                'tag': 'h5',
                'content': '1. Examine the First Two Edges:'
            },
            {
                'tag': 'p',
                'content': 'Look at the first two edges in the array.'
            },
            {
                'tag': 'h5',
                'content': '2. Identify the Common Node:'
            },
            {
                'tag': 'p',
                'content': 'The center node will be the one that appears in both edges. There are only three nodes involved in the first two edges, and two of them will be the same. That repeated node is the center.'
            },
            {
                'tag': 'h5',
                'content': '3. Return the Center Node:'
            },
            {
                'tag': 'p',
                'content': 'Once identified, return the center node.'
            },
            {
                'tag': 'h2',
                'content': 'Pseudo Code:'
            },
            {
                'tag': 'code',
                'content': '''
FUNCTION findCenter(edges)
    // e[0] and e[1] are the first two edges in the edges array
    IF edges[0][0] EQUALS edges[1][0] OR edges[0][0] EQUALS edges[1][1] THEN
        RETURN edges[0][0]
    ELSE
        RETURN edges[0][1]
    END IF
END FUNCTION'''
            },
            {
                'tag': 'h2',
                'content': 'Explanation:'
            },
            {
                'tag': 'ul',
                'content': ['The function findCenter checks if the first node in the first edge (edges[0][0]) is also present in the second edge (edges[1]). It does this by comparing edges[0][0] with both nodes in the second edge (edges[1][0] and edges[1][1]).','If edges[0][0] is found in the second edge, it is the center node, and the function returns edges[0][0].','If edges[0][0] is not found in the second edge, then the second node in the first edge (edges[0][1]) must be the center, and the function returns edges[0][1].']
            },
            {
                'tag': 'p',
                'content': 'This approach efficiently identifies the center of a star graph by leveraging the graph\'s structural properties, requiring only a constant number of comparisons.'
            }
        ],
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
        "_id": "LeetCode-Find-Median-from-Data-Stream",
        "href": "/solution/LeetCode-Find-Median-from-Data-Stream",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                'tag': 'p',
                'content': 'To solve this challenge, the key idea is to maintain two priority queues (or heaps): a max heap for the lower half of the numbers and a min heap for the upper half. This way, the max heap always contains the smaller half of the numbers, with its maximum value at the top, while the min heap contains the larger half of the numbers, with its minimum value at the top. By doing this, the median will always be among the top elements of these two heaps.'
            },
            {
                'tag': 'h2',
                'content': "Here's a step-by-step explanation of the solution, followed by the pseudo code:"
            },
            {
                'tag': 'h5',
                'content': '1. Initialization:'
            },
            {
                'tag': 'ul',
                'content': ['Initialize two heaps - a max heap (maxHeap) for the lower half of the numbers and a min heap (minHeap) for the upper half.']
            },
            {
                'tag': 'h5',
                'content': '2. Adding a Number (addNum):'
            },
            {
                'tag': 'ul',
                'content': [
                    "First, decide which heap to add the new number (num) to. If the maxHeap is empty or the new number is less than the maximum of the lower half (maxHeap's top), add it to the maxHeap. Otherwise, add it to the minHeap.",
                    "After adding the new number, check the size difference between the two heaps. The heaps should either have the same size or one heap should have one more element than the other. If the size difference exceeds 1, rebalance the heaps by moving the top element from the larger heap to the smaller heap."
                ]
            },
            {
                'tag': 'h5',
                'content': '3. Finding the Median (findMedian):'
            },
            {
                'tag': 'ul',
                'content': [
                    "If one heap has more elements than the other, the median is the top element of the heap with more elements.",
                    "If both heaps have the same number of elements, the median is the average of the tops of both heaps."
                ]
            },
            {
                'tag': 'h2',
                'content': 'Pseudo Code:'
            },
            {
                'tag': 'code',
                'content': '''
Class MedianFinder
    Initialize:
        maxHeap = new MaxHeap() // Lower half
        minHeap = new MinHeap() // Upper half

    Function addNum(num):
        If maxHeap.isEmpty() OR num < maxHeap.peek():
            maxHeap.add(num)
        Else:
            minHeap.add(num)
        
        // Rebalance heaps if necessary
        If maxHeap.size() - minHeap.size() > 1:
            minHeap.add(maxHeap.poll())
        Else If minHeap.size() - maxHeap.size() > 1:
            maxHeap.add(minHeap.poll())

    Function findMedian():
        If maxHeap.size() > minHeap.size():
            Return maxHeap.peek()
        Else If minHeap.size() > maxHeap.size():
            Return minHeap.peek()
        Else:
            Return (maxHeap.peek() + minHeap.peek()) / 2'''
            },
            {
                'tag': 'h2',
                'content': 'Optimization for Range-Based Data'
            },
            {
                'tag': 'p',
                'content': 'For the follow-up questions, if all integer numbers are in a specific range, you can optimize the solution by using an array or a hashmap to count the occurrences of each number. This would allow for a more efficient way to find the median without maintaining two heaps, especially when the range of numbers is small. For numbers mostly in a certain range with some outliers, a hybrid approach can be used where the array or hashmap is used for numbers within the range, and heaps or another data structure for numbers outside of the range.'
            }
        ],
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
        "_id": "LeetCode-Find-Mode-in-Binary-Search-Tree",
        "href": "/solution/LeetCode-Find-Mode-in-Binary-Search-Tree",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "The provided solution finds the mode(s) in a Binary Search Tree (BST) using a depth-first search (DFS) traversal and a hashmap (or object in JavaScript) to keep track of the frequency of each value encountered in the tree. Here's a step-by-step explanation followed by pseudo code:"
            },
            {
                "tag": "h2",
                "content": "Explanation:"
            },
            {
                "tag": "h5",
                "content": "1. Define a hashmap (memo):"
            },
            {

            },
            {
                "tag": "p",
                "content": "This hashmap is used to store the frequency of each value encountered in the tree. The keys are the node values, and the values are their respective counts."
            },
            {
                "tag": "h5",
                "content": "2. Depth-First Search (DFS) function:"
            },
            {
                "tag": "p",
                "content": "The dfs function is defined to traverse the tree. It's a recursive function that visits every node in the tree, starting from the root."
            },
            {
                "tag": "h5",
                "content": "3. Recursive DFS traversal:"
            },
            {
                "tag": "p",
                "content": "For each node visited, the function recursively calls itself on the left and right children of the node (if they exist), ensuring that all nodes in the tree are visited."
            },
            {
                "tag": "h5",
                "content": "4. Update hashmap:"
            },
            {
                "tag": "p",
                "content": "After visiting a node's children, the function updates the hashmap with the current node's value. If the value is already in the hashmap, its count is incremented. Otherwise, it's added to the hashmap with a count of 1."
            },
            {
                "tag": "h5",
                "content": "5. Sorting and finding modes:"
            },
            {
                "tag": "p",
                "content": "After the DFS traversal is complete, the entries in the hashmap are sorted in descending order by their frequency. The highest frequency (or frequencies, in case of a tie) determines the mode(s) of the tree."
            },
            {
                "tag": "h5",
                "content": "6. Constructing the result:"
            },
            {
                "tag": "p",
                "content": "The function then iterates through the sorted array of frequencies. It adds the values with the highest frequency to the result array. The iteration stops as soon as a value with a lower frequency is encountered, as the array is sorted."
            },
            {
                "tag": "h5",
                "content": "7. Return result:"
            },
            {
                "tag": "p",
                "content": "Finally, the function returns the result array, which contains the mode(s) of the BST."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
function findMode(root):
    Initialize a hashmap (memo) to store value frequencies
    Define a DFS function (dfs) that takes a node (n) as its argument

    DFS function (n):
        if n is null, return
        Call DFS on n.left (left child)
        Call DFS on n.right (right child)
        Update memo with n.val (increment if exists, set to 1 if not)

    Call DFS with root node
    Convert memo to an array of [value, frequency] pairs and sort it in descending order by frequency
    Initialize an empty array (ans) for storing modes
    Iterate through the sorted array:
        if current frequency equals the highest frequency, add the value to ans
        else, break the loop
    Return ans'''
            },
            {
                "tag": "h2",
                "content": "Note on Space Complexity:"
            },
            {
                "tag": "p",
                "content": "The follow-up question asks if it's possible to solve this without using any extra space. The provided solution does use extra space for the hashmap and the sorted array. An in-order traversal could be used to leverage the properties of the BST to find modes without extra space, but this would require a more complex approach to keep track of the current count, maximum count, and modes as you traverse."
            }
        ],
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
        "_id": "LeetCode-Find-the-Index-of-the-First-Occurrence-in-a-String",
        "href": "/solution/LeetCode-Find-the-Index-of-the-First-Occurrence-in-a-String",
        "video": {
            "has_video": False,
            "scripts": ["Video Script Goes Here", "Video2 Script Goes Here"]
        },
        "how_to": [
            {
                "tag": "p",
                "content": "To solve this coding challenge, the task is to find the first occurrence of a substring (needle) within another string (haystack). The solution provided uses a built-in JavaScript function indexOf, which directly solves the problem by returning the index of the first occurrence of the needle in the haystack. If the needle is not found, indexOf returns -1."
            },
            {
                "tag": "p",
                "content": "Let's break down the steps to solve this without relying on the built-in indexOf function, for a deeper understanding:"
            },
            {
                "tag": "h5",
                "content": "1. Check for Edge Cases:"
            },
            {
                "tag": "p",
                "content": "First, we need to handle some edge cases. If the needle is an empty string, we can consider the index of the first occurrence to be 0, since an empty string technically occurs at every index. If the haystack is empty, or if the needle is longer than the haystack, the needle cannot be found, so we return -1."
            },
            {
                "tag": "h5",
                "content": "2. Iterate Over the Haystack:"
            },
            {
                "tag": "p",
                "content": "Loop through the haystack string, up to the point where the remaining characters are at least as many as the length of the needle. This is because if there are fewer characters left in the haystack than the length of the needle, the needle cannot possibly fit."
            },
            {
                "tag": "h5",
                "content": "3. Match the Needle:"
            },
            {
                "tag": "p",
                "content": "For each character in the haystack that could potentially be the start of an occurrence of the needle, check if the substring of the haystack starting from that character, of the same length as the needle, matches the needle."
            },
            {
                "tag": "h5",
                "content": "4. Return the Index:"
            },
            {
                "tag": "p",
                "content": "If a match is found, return the current index. This is the first occurrence of the needle in the haystack."
            },
            {
                "tag": "h5",
                "content": "5. Return -1 if Not Found:"
            },
            {
                "tag": "p",
                "content": "If the loop completes and no match is found, return -1."
            },
            {
                "tag": "h2",
                "content": "Pseudo Code:"
            },
            {
                "tag": "code",
                "content": '''
FUNCTION findFirstOccurrence(haystack, needle)
    IF needle IS EMPTY
        RETURN 0  // An empty needle is found at the beginning

    FOR each startingPosition IN haystack FROM 0 TO LENGTH(haystack) - LENGTH(needle)
        matchFound = TRUE

        FOR each characterPosition IN needle FROM 0 TO LENGTH(needle) - 1
            IF haystack[startingPosition + characterPosition] != needle[characterPosition]
                matchFound = FALSE
                BREAK  // Exit the inner loop as soon as a mismatch is found

        IF matchFound
            RETURN startingPosition  // Return the index of the first match

    RETURN -1  // Return -1 if no match is found
END FUNCTION'''
            },
            {
                "tag": "p",
                "content": "This pseudo code provides a step-by-step approach to find the first occurrence of needle in haystack without using any built-in string search functions, demonstrating the underlying algorithmic logic."
            }
        ],
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

    return render_template('pages/career_guide/guide.html')


# 404 pg
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


# Code Solutions pg
@app.route('/code_solution/<solution_id>')
def code_solution(solution_id):
    """Display the Code Solution page."""

    context = {}

    for product in solutions_info:
        if product["_id"] == solution_id:
            context = product
            if not "search_res" in product:
                context["search_res"] = False
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