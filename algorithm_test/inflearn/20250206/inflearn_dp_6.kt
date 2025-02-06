import java.io.*
import kotlin.math.*
/*
    밑면 정사각형인 직육면체 벽돌 사용해 탑을 쌓는다.
    탑은 벽돌을 한 개씩 아래에서 위로

    조건1) 벽돌은 회전 x. 즉, 옆면을 밑면으로 사용 불가능
    조건2) 밑면의 넓이가 같은 벽돌 x 또한 무게가 같은 벽돌 x
    조건3) 벽돌들의 높이는 같을 수도 있다
    조건4) 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다
    조건5) 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다
*/
fun main() = with(File("inflearn_dp_6_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val bricks = mutableListOf<MutableList<Int>>()
    repeat(N){
        val index = readLine().split(" ").map { it.toInt() }.toMutableList()
        bricks.add(index)
    } 
    bricks.sortByDescending { it[0] }
    var dp = Array(N){ 0 }
    dp[0] = bricks[0][1]
    var res = bricks[0][1]
    println(bricks)


    for (i in 1 until N){
        var max_h = 0
        for (j in i-1 downTo 0){
            if (bricks[j][2] > bricks[i][2] && dp[j] > max_h){
                max_h = dp[j]
            }
        }
        println("max_h = ${max_h} bricks[i][1] = ${bricks[i][1]}")
        dp[i] = max_h + bricks[i][1]
        println(dp.contentToString())
        res = max(res, dp[i])
    }

    println(res)

}