import java.io.*
import kotlin.math.*
/*
    플로이드 워샬 알고리즘

*/

fun main() = with(File("inflearn_dp_12_input.txt").bufferedReader()){
    val(n, m) = readLine().split(" ").map{ it.toInt() }
    val dis = Array(n+1){ IntArray(n+1){ 5000 }}
    for (i in 1 until n+1){
        dis[i][i] = 0
    }
    for (i in 1 until m){
        val(a, b, c) = readLine().split(" ").map{ it.toInt() }
        dis[a][b] = c
    }

    // 플로이드워샬
    for (k in 1 until n+1){
        for(i in 1 until n+1){
            for (j in 1 until n+1){
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
            }
        }
    }

    // 출력
    for ( i in 1 until n+1){
        for (j in 1 until n+1){
            if (dis[i][j] == 5000){
                print("M ")
            } else {
                print("${dis[i][j]} ")
            }
        }
        println()
    }
}