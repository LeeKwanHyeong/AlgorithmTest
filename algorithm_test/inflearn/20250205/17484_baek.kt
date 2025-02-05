import java.io.*
import kotlin.math.*
/*
    백준 17484: [진우의 달 여행 (Small)]
    지구와 우주 사이는 NxM 행렬
    각 원소 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양

    1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 (-1, -1), (0, -1), (1, -1) 세가지.
    2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.

    [목표]: 연료를 최대한 아끼며 지구의 어느 위치에서든 출발하여 달의 어느 위치든 착륙하는 것
*/

fun main() = with(File("17484_input.txt").bufferedReader()){
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val grid = Array(N) { readLine().split(" ").map { it.toInt() } }
    
    val dp = Array(N) { Array(M) { IntArray(3) { Int.MAX_VALUE } } }

    // 초기화: 첫 번째 행에서 출발
    for (j in 0 until M) {
        for (dir in 0..2) {
            dp[0][j][dir] = grid[0][j]
        }
    }

    // DP 계산
    for (i in 1 until N) {
        for (j in 0 until M) {
            for (dir in 0..2) { // 현재 방향 (0:↙, 1:↓, 2:↘)
                for (prevDir in 0..2) { // 이전 방향
                    if (dir == prevDir) continue // 같은 방향 연속 금지

                    val prevCol = when (dir) {
                        0 -> j - 1  // ↙ 왼쪽 아래
                        1 -> j      // ↓ 아래
                        2 -> j + 1  // ↘ 오른쪽 아래
                        else -> j
                    }

                    // 범위 체크 및 유효성 검사
                    if (prevCol in 0 until M && dp[i-1][prevCol][prevDir] != Int.MAX_VALUE) {
                        dp[i][j][dir] = min(dp[i][j][dir], dp[i-1][prevCol][prevDir] + grid[i][j])
                    }
                }
            }
        }
    }

    // 마지막 행에서 최소 연료 찾기
    var result = Int.MAX_VALUE
    for (j in 0 until M) {
        for (dir in 0..2) {
            result = min(result, dp[N-1][j][dir])
        }
    }

    println(result)
}