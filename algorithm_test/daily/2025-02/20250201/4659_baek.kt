import java.io.*
/*
    가장 이상적인 해결법은 '발음이 가능한' 패스워드를 만드는 것
    FnordCom 패스워드 생성기 
    1. 모음(a,e,i,o,u) 하나를 반드시 포함
    2. 모음이 3개 혹은 자음이 3개 연속으로 나오면 안 된다.
    3. 같은 글자가 연속으로 두번 오면 안되나, ee, oo는 허용
*/

fun main() = with(File("4659_input.txt").bufferedReader()){
    val results = mutableListOf<String>()
    val vowels = setOf<String>("a", "e","i","o","u")

    while(true) {
        val password = readLine()

        if (password == "end") break

        var hasVowel = false
        var isAcceptable = true
        var consecutiveVowel = 0
        var consecutiveConsonant = 0
        var prevChar: Char? = null

        for (char in password) {
            // 모음  포함 여부
            if (char.toString() in vowels) {
                hasVowel = true
                consecutiveVowel++
                consecutiveConsonant = 0
            } else {
                consecutiveConsonant++
                consecutiveVowel = 0
            }

            // 모음 자음 3개 연속
            if (consecutiveVowel >= 3 || consecutiveConsonant >= 3){
                isAcceptable = false
                break
            }

            // 같은 글자 연속 두번 검사
            if (prevChar == char && char.toString() !in setOf("e", "o")){
                isAcceptable = false
                break
            }
            prevChar = char
        }
        if (hasVowel && isAcceptable) {
            println("<$password> is acceptable.")
        } else println("<$password> is not acceptable.")
    }
}