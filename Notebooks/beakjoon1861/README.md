# 백준 1861

경로 찾기

## 문제

N×N의 이차원 배열 A가 있고, A의 각 원소는 -100부터 100 사이의 임의의 정수 값을 갖는다. 이 이차원 배열의 `A[1][1]`부터 시작하여 `A[N][N]`에 이르는 경로를 선택하려 하는데, 아래와 같은 제약 조건이 있다.

상하좌우로 인접한 원소들을 방문해 나가야 한다. 즉 왼쪽, 오른쪽, 위쪽, 아래쪽의 네 가지 이동이 가능하다. 대각선으로는 이동이 불가능하다.
한 번 방문한 원소는 다시 방문할 수 없다.
이러한 제약을 만족하면서 임의의 경로를 따라 `A[N][N]`에 이르면 이 경로 상에 방문되었던 원소들의 값의 총합이 그 경로의 점수가 된다. 임의의 N×N 이차원 배열이 주어질 때, `A[1][1]`에서 `A[N][N]`에 이르는 경로의 점수를 최대화하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 이차원 배열의 크기를 나타내는 정수 N(3≤N≤100)이 주어진다. 다음 N개의 줄에는 각각의 N개의 정수(-100이상 100이하)가 빈 칸을 사이에 두고 주어지는데, 둘째 줄에는 A[1][1]～A[1][N], 셋째 줄에는 A[2][1]～A[2][N], … , N+1번째 줄에는 A[N][1]～A[N][N]의 값이 주어진다.

## 출력

첫째 줄에 프로그램이 구한 경로의 점수를 출력한다. 둘째 줄에는 이동 경로를 나타내는 문자들을 빈 칸을 사이에 두고 출력한다. 왼쪽은 L, 오른쪽은 R, 위쪽은 U, 아래쪽은 D로 나타내며, A[1][1]에서부터의 이동을 순서대로 출력하면 된다.