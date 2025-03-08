import java.io.*

/*
    노래 랭킹 리스트, 매번 게임할 때 마다 얻는 점수가 비오름차순으로 저장

    랭킹 리스트의 등수는 보통 위에서부터 몇 번째 있는 점수인지로 결정.
    * 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.

    N: 리스트에 있는 점수 N개 (비오름차순으로 주어짐)
    S: 태수의 새로운 점수
    P: 랭킹 리스트에 올라 갈 수 있는 점수의 개수
    
    * 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1 출력
    * 만약 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을때만 점수가 바뀐다.
*/

fun main() = with(File("1205_input.txt").bufferedReader()){
    // val (N, S, P) = readLine().split(' ').map{ it.toInt() }
    // var rankingList = if (N > 0) readLine().split(" ").map { it.toInt() } else listOf()

    // if (N==0){
    //     // 랭킹 리스트가 비어있는 경우
    //     println(1)
    //     return@with
    // }

    // if (N == P && S <= rankingList.last()){
    //     // 리스트가 꽉 차 있고, 태수의 점수가 가장 낮은 점수보다 작거나 같을 경우
    //     println(-1)    
    //     return@with
    // }

    // var rank = 1
    // for (i in rankingList.indices){
    //     if (S < rankingList[i]) {
    //         rank = i + 2 // 태수 점수가 작으면 순위는 i + 2
    //     } else break
    // }

    // if (N == P && rank > P){
    //     // 리스트가 꽉 차있고, 순위가 P보다 크면 랭킹에 못 들어감
    //     println(-1)
    // } else {
    //     println(rank)
    // }

    val (N, score, P) = readLine().split(" ").map { it.toInt() }
    val rankingList = if (N > 0) readLine().split(" ").map { it.toInt() } else listOf()

    when {
        N == 0 -> println(1)  // 빈 리스트의 경우 무조건 1등
        N == P && score <= rankingList.last() && score == rankingList.last() -> println(-1)  // 진입 불가
        else -> {
            val rank = rankingList.indexOfFirst { score >= it }.let { if (it == -1) N + 1 else it + 1 }
            if (N == P && rank > P) println(-1) else println(rank)
        }
    }

}