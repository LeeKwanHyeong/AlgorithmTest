import java.io.*
import kotlin.math.*
import java.util.*
data class State(val x: Int, val y: Int, val time: Int, val collected: Int)

fun main() = with(File("softier_together_input.txt").bufferedReader()){
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val grid = Array(n) { readLine()!!.split(" ").map { it.toInt() }.toIntArray() }
    val friends = Array(m) { readLine()!!.split(" ").map { it.toInt() - 1 } }

    val dx = arrayOf(0, 0, -1, 1)
    val dy = arrayOf(1, -1, 0, 0)
    
    var maxFruits = 0

    // 친구 별 BFS 탐색
    fun bfs(startX: Int, startY: Int): Int {
        val queue: Queue<State> = LinkedList()
        queue.add(State(startX, startY, 0, grid[startX][startY])) // 시작점에서 열매 수확

        val visited = Array(n) { BooleanArray(n) }
        visited[startX][startY] = true
        
        var maxCollect = 0

        while (queue.isNotEmpty()) {
            val (x, y, time, collected) = queue.poll()
            maxCollect = maxOf(maxCollect, collected)

            if (time == 3) continue // 3초 경과 시 종료

            for (dir in 0 until 4) {
                val nx = x + dx[dir]
                val ny = y + dy[dir]

                if (nx in 0 until n && ny in 0 until n && !visited[nx][ny]) {
                    queue.add(State(nx, ny, time + 1, collected + grid[nx][ny]))
                    visited[nx][ny] = true
                }
            }
        }
        return maxCollect
    }

    // 모든 친구에 대해 BFS 실행 후 최대 값 계산
    for (i in 0 until m) {
        val (x, y) = friends[i]
        maxFruits += bfs(x, y)
    }

    println(maxFruits)
}