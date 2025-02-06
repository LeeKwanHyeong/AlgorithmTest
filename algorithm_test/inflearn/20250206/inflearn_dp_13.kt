import java.io.*
import kotlin.math.*

/*
    회장 뽑기 (Floyd-Warshall Algorithm)

    월드컵 축구 모임 회장 선출
    회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 서로 알 수 있다.

    각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.
    1. 어느 회원이 다른 모든 회원과 친구이면 이 회원의 점수는 1
    2. 어느 회원의 점수가 2이면 다른 모든 회원이 친구 or 친구의 친구
    3. 어느 회원의 점수가 3이면, 다른 모든 회원이 친구 or 친구의 친구 or 친구의 친구의 친구
    ...

    * 각 회원의 점수를 정할 때 어떤 두 회원이 친구 사이이면서 동시에 친구의 친구 사이이면, 이 두사람은 친구
    회장은 가장 점수가 작은 사람이 된다.
*/
fun main() = with(File("inflearn_dp_13_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val dis = Array(N){ IntArray(N){ 100 } }
    var res = MutableList<Int>(N){ 0 }
    repeat(N+1){
        val (a, b) = readLine().split(" ").map { it.toInt() }
        dis[a-1][b-1] = 1
        dis[b-1][a-1] = 1
    }
    


    // Floyd-Warshall
    for (k in 0 until N){
        for (i in 0 until N){
            for (j in 0 until N){
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
            }
        }
    }

    var score = 100
    var out = mutableListOf<Int>()
    for (i in 0 until N){
        for(j in 0 until N){
            res[i] = max(res[i], dis[i][j])
        }
        score = min(score, res[i])
    }
    for (i in 0 until N){
        if(res[i] == score){
            out.add(i + 1)
        }
    }

    println("$score ${out.size}")
    println(out.joinToString(separator = " "))

    dis.forEach { println(it.contentToString()) }
}