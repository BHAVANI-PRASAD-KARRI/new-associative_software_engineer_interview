#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════╗
║   DSA Interview Quiz Tool — Associate SWE Prep   ║
╚══════════════════════════════════════════════════╝
"""

import random
import time
import json
import os
from datetime import datetime

# ─── ANSI Colors ───────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"

SCORE_FILE = os.path.join(os.path.dirname(__file__), "scores.json")

# ─── Question Bank ─────────────────────────────────────────────────────────────
QUESTIONS = {
    "Arrays & Strings": [
        {
            "q": "What is the time complexity of accessing an element in an array by index?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "answer": 2,
            "explanation": "Arrays store elements in contiguous memory. Index access is direct → O(1)."
        },
        {
            "q": "Which technique is used to find a subarray with a given sum in O(n)?",
            "options": ["Binary Search", "Sliding Window", "Divide and Conquer", "Backtracking"],
            "answer": 1,
            "explanation": "Sliding Window maintains a window of elements and adjusts it, solving subarray problems in O(n)."
        },
        {
            "q": "What does the Two Pointer technique primarily help with?",
            "options": [
                "Tree traversal",
                "Problems on sorted arrays or finding pairs",
                "Graph shortest path",
                "Hashing collisions"
            ],
            "answer": 1,
            "explanation": "Two Pointers use left/right pointers on sorted arrays to find pairs or partition in O(n)."
        },
        {
            "q": "What is the worst-case time complexity of searching in an unsorted array?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
            "answer": 2,
            "explanation": "Without sorting or hashing, you must scan every element → O(n)."
        },
        {
            "q": "Which of the following reverses a string most efficiently in Python?",
            "options": ["for loop", "s[::-1]", "reversed(s)", "s.reverse()"],
            "answer": 1,
            "explanation": "s[::-1] uses slicing with step -1 — the most Pythonic and efficient way to reverse a string."
        },
    ],
    "Linked Lists": [
        {
            "q": "What is the time complexity of inserting at the head of a singly linked list?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "answer": 2,
            "explanation": "You just update the head pointer — no traversal needed → O(1)."
        },
        {
            "q": "Which algorithm detects a cycle in a linked list in O(1) space?",
            "options": ["BFS", "DFS", "Floyd's Cycle Detection (Fast & Slow pointers)", "Hashing nodes"],
            "answer": 2,
            "explanation": "Floyd's algorithm uses two pointers (slow=1 step, fast=2 steps). If they meet, a cycle exists."
        },
        {
            "q": "To find the middle of a linked list in one pass, you use:",
            "options": ["Two stacks", "Slow and fast pointers", "Recursion", "Hashing"],
            "answer": 1,
            "explanation": "Fast pointer moves 2x speed of slow. When fast reaches end, slow is at the middle."
        },
        {
            "q": "What is the main disadvantage of a singly linked list over an array?",
            "options": [
                "Slower insertion at head",
                "Fixed size",
                "No random access — O(n) to reach index i",
                "Can't store integers"
            ],
            "answer": 2,
            "explanation": "Unlike arrays, linked lists have no index-based access. You must traverse from head → O(n)."
        },
        {
            "q": "Which data structure is typically used to reverse a linked list iteratively?",
            "options": ["Queue", "Stack", "Three pointers (prev, curr, next)", "HashMap"],
            "answer": 2,
            "explanation": "Iterative reversal uses prev=None, curr=head, next pointer to reverse links one by one."
        },
    ],
    "Stacks & Queues": [
        {
            "q": "What principle does a Stack follow?",
            "options": ["FIFO", "LIFO", "LILO", "Priority-based"],
            "answer": 1,
            "explanation": "Stack = Last In, First Out. The last element pushed is the first to be popped."
        },
        {
            "q": "Which data structure is best for implementing a BFS traversal?",
            "options": ["Stack", "Queue", "Heap", "Array"],
            "answer": 1,
            "explanation": "BFS explores level by level. A Queue (FIFO) naturally processes nodes in the order they are discovered."
        },
        {
            "q": "What is the time complexity of push and pop in a stack?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
            "answer": 2,
            "explanation": "Both push and pop only touch the top of the stack → O(1)."
        },
        {
            "q": "A stack can be used to check:",
            "options": [
                "Shortest path in a graph",
                "Balanced parentheses in an expression",
                "Maximum element in a stream",
                "Level order traversal"
            ],
            "answer": 1,
            "explanation": "Push opening brackets, pop on closing. If stack is empty at end and each match is valid → balanced."
        },
        {
            "q": "Which Python built-in can be used as a queue efficiently?",
            "options": ["list", "tuple", "collections.deque", "set"],
            "answer": 2,
            "explanation": "collections.deque supports O(1) appendleft() and popleft(), unlike list which is O(n) for popleft."
        },
    ],
    "Trees & BST": [
        {
            "q": "What is the height of a balanced BST with n nodes?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "answer": 1,
            "explanation": "A balanced BST splits nodes evenly at each level → height = O(log n)."
        },
        {
            "q": "In which tree traversal do you visit: Left → Root → Right?",
            "options": ["Preorder", "Postorder", "Inorder", "Level Order"],
            "answer": 2,
            "explanation": "Inorder (Left→Root→Right) of a BST gives elements in sorted ascending order."
        },
        {
            "q": "What is the time complexity of search in a balanced BST?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
            "answer": 1,
            "explanation": "Each step eliminates half the tree → O(log n), similar to binary search."
        },
        {
            "q": "Which traversal is used to delete a tree (free memory)?",
            "options": ["Preorder", "Inorder", "Postorder", "Level Order"],
            "answer": 2,
            "explanation": "Postorder (Left→Right→Root) processes children before parent, safe for deletion."
        },
        {
            "q": "The Lowest Common Ancestor (LCA) of two nodes in a BST can be found in:",
            "options": ["O(n²)", "O(n log n)", "O(log n) for balanced BST", "O(1)"],
            "answer": 2,
            "explanation": "Traverse from root: if both nodes are smaller go left, if both larger go right, else current node is LCA."
        },
    ],
    "Graphs": [
        {
            "q": "What data structure does BFS use internally?",
            "options": ["Stack", "Queue", "Heap", "Set"],
            "answer": 1,
            "explanation": "BFS uses a Queue to process nodes level by level (FIFO order)."
        },
        {
            "q": "What data structure does DFS use internally (iterative version)?",
            "options": ["Queue", "Stack", "Heap", "Deque"],
            "answer": 1,
            "explanation": "DFS explores as deep as possible. A Stack (LIFO) naturally backtracks when needed."
        },
        {
            "q": "Dijkstra's algorithm is used to find:",
            "options": [
                "Minimum spanning tree",
                "Shortest path in a weighted graph (no negative weights)",
                "Topological order",
                "Cycle detection"
            ],
            "answer": 1,
            "explanation": "Dijkstra finds the shortest path from a source to all nodes. Doesn't work with negative weights."
        },
        {
            "q": "Topological sorting is applicable to:",
            "options": [
                "Any graph",
                "Undirected graphs only",
                "Directed Acyclic Graphs (DAGs)",
                "Weighted graphs only"
            ],
            "answer": 2,
            "explanation": "Topological sort orders nodes so every directed edge u→v has u before v. Only valid on DAGs."
        },
        {
            "q": "Time complexity of BFS/DFS where V = vertices, E = edges:",
            "options": ["O(V²)", "O(V + E)", "O(E log V)", "O(V log V)"],
            "answer": 1,
            "explanation": "Every vertex and edge is visited exactly once → O(V + E)."
        },
    ],
    "Dynamic Programming": [
        {
            "q": "What are the two key properties a problem must have for DP?",
            "options": [
                "Greedy choice + optimal substructure",
                "Overlapping subproblems + optimal substructure",
                "Divide and conquer + memoization",
                "Recursion + hashing"
            ],
            "answer": 1,
            "explanation": "DP requires: (1) overlapping subproblems — same sub-problems recur, and (2) optimal substructure — optimal solution built from optimal sub-solutions."
        },
        {
            "q": "What is memoization in DP?",
            "options": [
                "Bottom-up table filling",
                "Storing results of expensive function calls to avoid recomputation",
                "Sorting the input before solving",
                "Reducing space complexity"
            ],
            "answer": 1,
            "explanation": "Memoization = Top-down DP. Cache results of subproblems so they're not recomputed."
        },
        {
            "q": "The classic 0/1 Knapsack problem has a DP time complexity of:",
            "options": ["O(n log n)", "O(n²)", "O(n × W) where W is knapsack capacity", "O(2ⁿ)"],
            "answer": 2,
            "explanation": "We build a 2D DP table of size n×W, filling each cell in O(1) → total O(n×W)."
        },
        {
            "q": "Which problem is solved using the Longest Common Subsequence (LCS) DP approach?",
            "options": [
                "Shortest path in a graph",
                "Diff tools, DNA sequencing — finding common sequences in two strings",
                "Sorting an array",
                "Finding cycles in a graph"
            ],
            "answer": 1,
            "explanation": "LCS finds the longest subsequence common to both strings. Used in diff tools, bioinformatics, etc."
        },
        {
            "q": "Fibonacci using DP reduces time complexity from ___ (naive recursion) to ___:",
            "options": ["O(n) → O(1)", "O(2ⁿ) → O(n)", "O(n²) → O(n)", "O(n log n) → O(n)"],
            "answer": 1,
            "explanation": "Naive recursion recomputes fib(n-1), fib(n-2) repeatedly → O(2ⁿ). DP stores results → O(n)."
        },
    ],
    "Sorting & Searching": [
        {
            "q": "What is the average time complexity of QuickSort?",
            "options": ["O(n²)", "O(n log n)", "O(n)", "O(log n)"],
            "answer": 1,
            "explanation": "QuickSort averages O(n log n) with a good pivot. Worst case (sorted array, bad pivot) = O(n²)."
        },
        {
            "q": "Which sorting algorithm is stable AND has O(n log n) worst case?",
            "options": ["QuickSort", "HeapSort", "MergeSort", "SelectionSort"],
            "answer": 2,
            "explanation": "MergeSort is stable (preserves relative order of equal elements) and always O(n log n)."
        },
        {
            "q": "Binary Search requires the array to be:",
            "options": ["Unsorted", "Sorted", "Filled with distinct elements", "Of even length"],
            "answer": 1,
            "explanation": "Binary Search works by comparing the middle element and discarding half the array — only valid on sorted arrays."
        },
        {
            "q": "What is the time complexity of Binary Search?",
            "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
            "answer": 2,
            "explanation": "Each step halves the search space. For n elements, you need at most log₂(n) steps → O(log n)."
        },
        {
            "q": "Counting Sort is efficient when:",
            "options": [
                "Input is a list of floating point numbers",
                "Input range k is small and known (integers)",
                "Input is already sorted",
                "Input has many duplicate strings"
            ],
            "answer": 1,
            "explanation": "Counting Sort runs in O(n + k) where k is the range of values. Best when k is small."
        },
    ],
    "Hashing": [
        {
            "q": "What is the average time complexity of insert, delete, and search in a HashMap?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
            "answer": 2,
            "explanation": "Hash functions map keys to indices directly → O(1) average for all operations."
        },
        {
            "q": "What is a hash collision?",
            "options": [
                "Two keys with the same value",
                "Two different keys mapping to the same hash index",
                "A hash function returning null",
                "An overflow in the hash table"
            ],
            "answer": 1,
            "explanation": "Collision = two different keys → same bucket. Handled by chaining (linked list) or open addressing."
        },
        {
            "q": "Which Python data structure implements a hash map?",
            "options": ["list", "tuple", "dict", "set"],
            "answer": 2,
            "explanation": "Python's dict is a hash map — keys are hashed for O(1) average access."
        },
        {
            "q": "Finding two numbers in an array that sum to a target is solved most efficiently using:",
            "options": ["Nested loops O(n²)", "Sorting + binary search O(n log n)", "HashMap O(n)", "Recursion"],
            "answer": 2,
            "explanation": "Store each element in a HashMap. For each element x, check if (target - x) exists → O(n)."
        },
        {
            "q": "Worst-case time complexity of HashMap operations (due to collisions) is:",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
            "answer": 2,
            "explanation": "In the worst case (all keys hash to same bucket), lookup degrades to O(n) linked list traversal."
        },
    ],
}

# ─── Helpers ───────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════╗
║        DSA Interview Quiz — Associate SWE Prep       ║
║              Python CLI Edition  🐍                  ║
╚══════════════════════════════════════════════════════╝{RESET}
""")

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE) as f:
            return json.load(f)
    return []

def save_score(topic, score, total, duration):
    scores = load_scores()
    scores.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "topic": topic,
        "score": score,
        "total": total,
        "percent": round(score / total * 100, 1),
        "duration_sec": round(duration, 1)
    })
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def show_leaderboard():
    scores = load_scores()
    if not scores:
        print(f"\n{YELLOW}No scores yet. Complete a quiz first!{RESET}\n")
        return
    print(f"\n{BOLD}{CYAN}{'─'*55}")
    print(f"  📊  Score History")
    print(f"{'─'*55}{RESET}")
    print(f"  {'Date':<18} {'Topic':<22} {'Score':<10} {'%'}")
    print(f"  {'─'*16} {'─'*20} {'─'*8} {'─'*6}")
    for s in scores[-10:]:
        pct = s['percent']
        color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)
        print(f"  {s['date']:<18} {s['topic']:<22} {s['score']}/{s['total']:<6}   {color}{pct}%{RESET}")
    print()

def pick_option(prompt, options):
    for i, opt in enumerate(options, 1):
        print(f"  {CYAN}[{i}]{RESET} {opt}")
    while True:
        try:
            choice = int(input(f"\n{BOLD}→ {prompt}: {RESET}").strip())
            if 1 <= choice <= len(options):
                return choice - 1
        except (ValueError, KeyboardInterrupt):
            pass
        print(f"{RED}  Invalid choice. Enter a number between 1 and {len(options)}.{RESET}")

def run_quiz(topic, questions, timed=False):
    clear()
    print_banner()
    print(f"{BOLD}{BLUE}  Topic : {topic}{RESET}")
    print(f"  Questions : {len(questions)}")
    print(f"  Mode  : {'⏱  Timed (30s per question)' if timed else '📖  Untimed'}")
    print(f"\n{CYAN}{'─'*55}{RESET}\n")
    input(f"  Press {BOLD}Enter{RESET} to start...\n")

    score = 0
    wrong = []
    start_time = time.time()

    for idx, q in enumerate(questions, 1):
        clear()
        print(f"{CYAN}{BOLD}  Q{idx}/{len(questions)} — {topic}{RESET}")
        print(f"\n  {BOLD}{q['q']}{RESET}\n")

        for i, opt in enumerate(q["options"]):
            print(f"  {CYAN}[{i+1}]{RESET} {opt}")

        if timed:
            q_start = time.time()
            print(f"\n  {YELLOW}⏱  You have 30 seconds!{RESET}")

        ans = None
        while ans is None:
            try:
                raw = input(f"\n{BOLD}  Your answer (1-{len(q['options'])}): {RESET}").strip()
                val = int(raw)
                if 1 <= val <= len(q["options"]):
                    ans = val - 1
            except (ValueError, KeyboardInterrupt):
                pass

        if timed:
            elapsed = time.time() - q_start
            if elapsed > 30:
                print(f"\n  {RED}⏰ Time's up!{RESET}")

        if ans == q["answer"]:
            print(f"\n  {GREEN}{BOLD}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"\n  {RED}{BOLD}❌ Wrong!{RESET}  Correct answer: {CYAN}{q['options'][q['answer']]}{RESET}")
            wrong.append(q)

        print(f"  {YELLOW}💡 {q['explanation']}{RESET}")
        input(f"\n  {BOLD}Press Enter for next question...{RESET}")

    duration = time.time() - start_time
    clear()
    print_banner()

    pct = round(score / len(questions) * 100, 1)
    bar = "█" * int(pct // 5) + "░" * (20 - int(pct // 5))
    color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)

    print(f"""
{BOLD}{CYAN}  ╔══════════════════════════════╗
  ║        Quiz Complete! 🎉      ║
  ╚══════════════════════════════╝{RESET}

  Topic    : {BOLD}{topic}{RESET}
  Score    : {color}{BOLD}{score} / {len(questions)}{RESET}
  Result   : {color}{bar} {pct}%{RESET}
  Duration : {round(duration, 1)}s
""")

    if pct >= 80:
        print(f"  {GREEN}{BOLD}🏆 Excellent! You're interview-ready on this topic!{RESET}")
    elif pct >= 60:
        print(f"  {YELLOW}{BOLD}📚 Good effort! Review the wrong answers below.{RESET}")
    else:
        print(f"  {RED}{BOLD}💪 Keep practicing — you'll get there!{RESET}")

    if wrong:
        print(f"\n{BOLD}{RED}  ── Questions to Review ──{RESET}")
        for w in wrong:
            print(f"\n  {YELLOW}Q: {w['q']}{RESET}")
            print(f"  {GREEN}A: {w['options'][w['answer']]}{RESET}")
            print(f"  {CYAN}💡 {w['explanation']}{RESET}")

    save_score(topic, score, len(questions), duration)
    input(f"\n  {BOLD}Press Enter to return to menu...{RESET}")

# ─── Main Menu ─────────────────────────────────────────────────────────────────

def main():
    topics = list(QUESTIONS.keys())

    while True:
        clear()
        print_banner()
        print(f"{BOLD}  Choose an option:{RESET}\n")
        print(f"  {CYAN}[1]{RESET} 📝  Quiz by Topic")
        print(f"  {CYAN}[2]{RESET} 🎲  Random Mixed Quiz (all topics)")
        print(f"  {CYAN}[3]{RESET} ⏱   Timed Quiz (30s per question)")
        print(f"  {CYAN}[4]{RESET} 📊  View Score History")
        print(f"  {CYAN}[5]{RESET} 🚪  Exit\n")

        try:
            choice = input(f"{BOLD}→ Enter choice (1-5): {RESET}").strip()
        except KeyboardInterrupt:
            print(f"\n{YELLOW}  Goodbye! Good luck with your interviews! 🚀{RESET}\n")
            break

        if choice == "1":
            clear()
            print_banner()
            print(f"{BOLD}  Select a DSA Topic:\n{RESET}")
            topic_idx = pick_option("Select topic", topics)
            topic = topics[topic_idx]
            questions = QUESTIONS[topic][:]
            random.shuffle(questions)
            run_quiz(topic, questions, timed=False)

        elif choice == "2":
            all_q = []
            for qs in QUESTIONS.values():
                all_q.extend(qs)
            random.shuffle(all_q)
            run_quiz("Mixed — All Topics", all_q[:15], timed=False)

        elif choice == "3":
            clear()
            print_banner()
            print(f"{BOLD}  Timed Quiz — Select a Topic:\n{RESET}")
            topic_idx = pick_option("Select topic", topics)
            topic = topics[topic_idx]
            questions = QUESTIONS[topic][:]
            random.shuffle(questions)
            run_quiz(topic, questions, timed=True)

        elif choice == "4":
            clear()
            print_banner()
            show_leaderboard()
            input(f"  {BOLD}Press Enter to return to menu...{RESET}")

        elif choice == "5":
            print(f"\n{GREEN}{BOLD}  Goodbye! Best of luck with your interviews! 🚀{RESET}\n")
            break

if __name__ == "__main__":
    main()
