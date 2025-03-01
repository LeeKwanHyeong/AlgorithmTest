import java.util.*
import java.io.*

// fun main() {
//     val path = "input.txt"
//     val reader = BufferedReader(FileReader(File(path)))

//     val T = reader.readLine().toInt()
    

//     repeat(T){
//         val target = reader.readLine().toInt()

//         val s_target = target.toString().substring(2).toInt()
//         val task = (target + 1)

//         if (task % s_target == 0){
//             println("Good")
//         } else println("Bye")
//     }
// }

fun main() = with(File("input.txt").bufferedReader()){
    val T = readLine()!!.toInt()

    repeat(T) {
        val target = readLine().toInt()

        val s_target = target.toString().substring(2).toInt()
        val task = (target + 1)
        if (task % s_target == 0) {
            println("Good")
        } else println("Bye")
    }
}