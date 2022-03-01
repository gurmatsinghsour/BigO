 <p align="center"> <a href = "https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/"> <img src = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/mypic.png"> </p> </a>

<p align="center" style="font-size:16px; color:lightgreen;"> 
BIG O - Asymptotic Notation </p>

<p align="center"> It's basically used to measure the performance i.e the time complexity or space complexity required on your code </p>
 

There are different types of Big Os 

1. O(1) -> Constant with no loops. Only one element is operated from an array, no matter how big.  
2. O(log N) - > #learning
3. O(n) -> Linear (for loops, while loops through n times ) 
4. O(n log (n)) -> #learning
5. O(n^2) -> Quadratic. When every elements in a collection which needs to be compared to every other element in an array is O(n^2) or when there are two nested loops.
6. O(2^n) -> #learning



Rules to considers. 

1. Always worst Case
2. Remove Constants
3. Different inputs should have different variables: O(a + b) & A and B arrays nested would be: O(a * b)
   + for steps in order
   * for nested steps
4. Drop Non-dominant terms
</p>