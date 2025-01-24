import java.io.*

/*
    순위
    1. 금메달 수가 더 많은 나라
    2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
    3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

    문제: 어느 국가가 몇등 했는지 말하라.
    K 국가의 등수는?
 */
fun main() = with(File("input.txt").bufferedReader()) {
    val (N, K) = readLine().split(" ").map{ it.toInt() }
    val map: Map<int, List<int>> = Map()

    repeat(N){
        val step = readLine().split(" ").map { it.toInt() }
        
    }
}