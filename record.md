# 2024-05-17 CF round 945

Brute force
Divide and conquer
Search and enumeration
dynamic programming


## A 
### Active
1. 무엇이 변하지 않는가? &rarr; 세 플레이어 점수의 합의 홀짝성 &rarr; valid함을 판단하는 기준은 세 플레이어 점수의 합의 홀짝성  

### Passive
1. 그렇다면 무승부의 최대 개수는 어떻게 구할까? 
- case1 작은 두 수의 합이 큰 수보다 크거나 같을 경우 &rarr; 모든 경기가 비긴 경우의 수 가능.
- case2 그렇지 않을 경우 &rarr; 작은 점수의 플레이어 2명이 모든 경기를 비긴 경우의 수 가능.

## B 
### Active
1. array 의 모든 인접한 k 개의 수를 bitwise OR 했을 때 모두 같은 값이 나와야 한다 &rarr; 그렇다면 array 의 모든 수를 bitwise OR 한 값 또한 같은 값이어야 한다. (귀류법)

### passive
1. 그렇다면 그러한 수 k 의 최소값을 어떻게 구할까? 
- brute force : 모든 가능한 k 에 대하여 조건 성립을 확인해 k 의 최솟값을 구해볼까? &rarr; k(1~n) 각 값에 대하여 (1~n)개 숫자의 bitwise operation 을 (n~1)번 해야하므로 시간 복잡도 O(n^3) &rarr; 불가능.  

- array 의 모든 수를 이진수로 표현했을 떄, 최대 20 자리 이진수로 표현되고 각 자리를 나누어서 생각했을 때, 각 자리에 1을 가진 수가 m 거리만큼 떨어져 있다면, k 는 최소한 m 보다는 크거나 같아야 한다. (k가 m 보다 작으면, 최소 1가지 경우의 bitwise OR  결과는 해당 자리에 1을 가질 수 없기 때문) &rarr; 그렇다면 각 자리마다 최대로 떨어진 거리를 구하여 각 거리의 최대 값이 k 의 최소값이 되겠네.

## C
### Active
1. permutation 의 개수는 n! 이므로 brute force 는 어렵겠네.
2. 그렇다면 주어진 permutation 을 보고 특정 기준에 따라서 새로운 permutation 의 각 자리에 숫자를 채워넣으면 되겠다.
3. 최대한의 local maxima 를 만드려면, 숫자가 작았다가 크고를 최대한 반복해야 하겠네.
&rarr; maxima가 되어야 할 자리엔 큰 수를 배치하고 그 옆자리엔 작은 수를 배치한다면, 항상 최대 숫자의 local maxima 를 만들 수 있지 않을까?

### Passive
1. 그렇다면, Maxima가 될 자리는 어떻게 정할까? &rarr; 확률적으로 가장 큰 수가 있는 자리를 기준으로 정하는게 local maxima를 만들기 수월할 것 같다. &rarr; 그렇다면 local maxima가 될 자리에는 n/2 를 배치하고 그 옆자리에는 0~n/2를 배치해야겠네. 그리고 숫자를 최대한 고르게 분포시키기 위해서 가장 큰수에 가장 작은 수를 배치해야겠네.

2. 그런데, 최대 숫자의 local maxima가 나오지 않을 수도 있나? &rarr; 최악의 경우의 수를 생각해보자   
arr: 5 10 9 1 8 2 7 3 6 4   
ans: 5 6 1 10 2 9 3 8 4 7  
sum: 10 16 10 11 10 11 10 11 10 11  
최악의 경우에도 local maxima가 n//2 - 1 개 만큼 만들어지네. 완벽한 증명은 아니지만 충분히 사용할 수 있겠어.




