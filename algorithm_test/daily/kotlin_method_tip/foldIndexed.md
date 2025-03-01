# 📚 Kotlin `foldIndexed` 완벽 가이드

---

## ✅ 1️⃣ `foldIndexed`란?

- `foldIndexed`는 Kotlin의 **고차 함수**로, 컬렉션을 순회하면서 누적(accumulate) 작업을 수행할 수 있는 강력한 도구입니다.
- `fold` 함수의 확장 버전으로, **현재 인덱스(index)**를 추가로 제공하여 인덱스를 활용한 누적 작업이 가능합니다.

---

## 🚀 2️⃣ 기본 문법

```kotlin
list.foldIndexed(initial: T, operation: (index: Int, acc: T, element: E) -> T)
```
- `initial`: 누적값의 초기값
- `operation`: 각 요소에 적용할 람다 함수
  - `index`: 현재 요소의 인덱스
  - `acc`: 누적된 결과값(accumulator)
  - `element`: 현재 요소

## 🚀 3️⃣ 간단한 예제
### 예제1: 인덱스와 값을 누적하기
```kotlin
val numbers = listOf(1, 2, 3, 4, 5)

val result = numbers.foldIndexed(0) { index, acc, value ->
    acc + (index * value)
}

println(result) // 출력: 40
```
### 예제2: 인덱스와 값을 누적하기
```kotlin
val words = listOf("Kotlin", "Java", "Python")

val result = words.foldIndexed("") { index, acc, word ->
    acc + "${index + 1}. $word\n"
}

println(result)
1. Kotlin
2. Java
3. Python
```

## 🚀 4️⃣ 자주 사용하는 활용 예제
### 예제1: 리스트의 짝수 인덱스 요소만 합하기
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)

val evenIndexSum = numbers.foldIndexed(0) { index, acc, value ->
    if (index % 2 == 0) acc + value else acc
}

println(evenIndexSum) // 출력: 9 (1 + 3 + 5)

```
### 예제2: 최대값의 인덱스 찾기
```kotlin
val numbers = listOf(3, 8, 2, 5, 10, 4)

val maxIndex = numbers.foldIndexed(Pair(0, Int.MIN_VALUE)) { index, acc, value ->
    if (value > acc.second) Pair(index, value) else acc
}.first

println(maxIndex) // 출력: 4 (값 10의 인덱스)
```