import java.io.*

/*
    쿠키 버튼은 점프, 슬라이드 2가지
    머리: 심장 바로 위칸 1칸 크기로
    왼팔: 심장 바로 왼칸
    오른팔: 심장 바로 오른칸
    허리: 심장 바로 아래칸
    왼다리: 심장 바로 왼쪽 아래 (왼쪽 대각선)
    오른다리: 심장 바로 오른쪽 아래 (오른쪽 대각선)
    * 허리, 팔, 다리 길이는 무조건 길이, 너비 무조건 1이상
*/

fun main() = with(File("20125_input.txt").bufferedReader()){
    val N = readLine().toInt()
    var space = mutableListOf<List<Char>>()
    var heart = Pair(0, 0)
    var leftArm = 0
    var rightArm = 0
    var back = 0
    var leftLeg = 0
    var rightLeg = 0
   
    repeat(N){
        val row = readLine().toList()
        space.add(row)
    }
    println(space)

    outer@ for (i in 0..N-1){
        for (j in 0..N-1){
            if(space[i][j].toString() == "*") {
                heart = Pair(i+1, j)
                break@outer
            }
        }
    }
    println(heart)

    // Left Arm
    for (i in 0..heart.second){
        if(space[heart.first][i].toString() == "*") leftArm++
    }

    // Right Arm
    for (i in heart.second..N-1){
        if(space[heart.first][i].toString() == "*") rightArm++
    }

    // Back
    for (i in heart.first..N-1){
        // Back
        if(space[i][heart.second].toString() == "*") back++
        // Left Leg
        if(space[i][heart.second - 1].toString() == "*") leftLeg++
        // Right Leg
        if(space[i][heart.second + 1].toString() == "*") rightLeg++
    }

    println("${heart.first + 1} ${heart.second + 1}")
    print("${leftArm-1} ${rightArm - 1} ${back - 1} ${leftLeg - 1} ${rightLeg - 1}")
}