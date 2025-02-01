import java.io.*

/*
    미니 게임 목록
    Y : 윷놀이 (2명이서 게임)
    F : 같은 그림 찾기 (3명이서 게임)
    O : 원카드 (4명이서 게임)

    N : 임스와 같이 플레이하기를 신청한 횟수
    K : 게임 종류

    최대 몇번이나 임스와 함께 게임을 할 수 있나?
    1. 여러번 게임을 플레이하고자 하는 사람은 있으나, 한 번 플레이한 사람과는 다시 플레이 하지 않음
*/

fun main() = with(File("25757_input.txt").bufferedReader()){
    val (N, K) = readLine().split(" ")
    val gameSet = mutableSetOf<String>()

    repeat(N.toInt()){
        val id = readLine()
        gameSet.add(id)
    }

    when(K){
        "Y" -> {
            print(gameSet.size)
        }
        "F" -> {
            print(gameSet.size / 2)
        }
        "O" -> {
            print(gameSet.size / 3)
        }
    }

}