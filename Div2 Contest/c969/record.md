# 2024-08-30 CF round 969


## A 
### Active
3개 뽑는데 서로 다 서로소 
무조건 홀수 2개 짝수 1개 또는 홀수 3개
### Passive

## B 
### Active
최댓값만 고려하면됨
### passive

## C
### Active
결국 최대공약수 크기만큼 마음대로 조작할 수 있는 상황과 등가임
### Passive

## D
### Active
score 구하는거는 dfs 1번으로 끝 
optimal 하게 채우는걸 어떻게? 
각 점에서 weight 는 최대가 1임.(root 와 leaf value 가 같으면 0, 아니면 1)
1. leaf 를 구한다. 
2. leaf 중에 정해진 값이 아무것도 없다면 root 를 0으로 채운다.
2. leaf 중에 정해진 값이 있다면 root 를 leaf value 중 다수의 값과 반대로 채운다.
3. 나머지 leaf 중 하나를 root 와 같게 채운다.

* 보통은 leaf나 root 에 먼저 채우는게 이득이나, leaf의 상황이 같고 root 가 비어 있을때, 선빵치면 진다.

### Passive


