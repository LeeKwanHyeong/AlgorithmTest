import java.io.*
import kotlin.collections.*
/*
    1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 
    1: 스위치 켜져있음 0: 스위치 꺼져있음

    * 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 줌

    남학생은, 스위치 번호가 자기가 받은 수의 배수 => 그 스위치의 상태를 바꾼다.
    여학생은, 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 
    "가장 많은 스위치"를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
    
    
*/

fun main() = with(File("1244_input.txt").bufferedReader()){

    val switches = readLine().toInt() /// 스위치 개수
    val switchState = readLine().split(" ").map { it.toInt() }.toMutableList() // 스위치 상태
    val students  = readLine().toInt() // 학생 수

    switchState.add(0, 0)

    repeat(students){
        val (sex, index) = readLine().split(" ").map{ it.toInt() }
        var i = 0
        when(sex){
            1 -> { // 남학생
                i++
                while((index) * i <= switchState.size - 1) {
                    switchState[(index ) * i] = if(switchState[(index) * i] == 0) 1 else 0
                    i++
                }
            }
            2 -> { // 여학생
                while(index + i <= switchState.size - 1 && index - i >= 0){
                    if (index == 1){
                        switchState[1] = if(switchState[1] == 0) 1 else 0
                        break
                    }
                    else if(switchState[index + i] == switchState[index - i] && index - i != 0){
                        val checker = switchState[index + i]
                        switchState[index + i] = if(checker == 0) 1 else 0
                        switchState[index - i] = if(checker == 0) 1 else 0
                        i++
                    } else {
                        break
                    }
                }
            }
        }
    }

    switchState.remove(0)
    switchState.chunked(20).forEach { chunk -> 
        println(chunk.joinToString(" "))
    }
}