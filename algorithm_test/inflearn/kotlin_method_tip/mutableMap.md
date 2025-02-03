# 🚀 Kotlin의 `getOrPut`와 유사한 함수들 정리

Kotlin의 `getOrPut`은 `MutableMap`에서 자주 사용되는 함수로, 키가 존재하면 값을 반환하고, 존재하지 않으면 새 값을 생성하여 추가하는 역할을 합니다. 이 외에도 Kotlin 컬렉션에서 자주 사용하는 유사한 함수들이 있습니다.

---

## ✅ 1️ `getOrPut`

### 📌 설명
- **동작:** 키가 존재하면 해당 값을 반환, 없으면 생성한 후 반환
- **사용 대상:** `MutableMap`

### 📋 문법
```kotlin
map.getOrPut(key) { defaultValue }
```

### 예제
```kotlin
fun main() {
    val map = mutableMapOf<String, Int>()

    // "apple" 키가 없으므로 1을 추가하고 반환
    println(map.getOrPut("apple") { 1 })  // 출력: 1

    // "apple" 키가 있으므로 기존 값 반환
    println(map.getOrPut("apple") { 100 })  // 출력: 1

    println(map)  // 결과: {apple=1}
}
```
### 사용 사례
1. 빈도가 높은 데이터를 카운트 할 때 유용
2. 리스트 초기화가 필요한 경우

---


## ✅ 2 `putIfAbsent`

### 📌 설명
- **동작:** 키가 없을 때만 값을 추가
- `getOrPut`과 유사하지만 ***값을 반환하지 않고 추가 여부만 확인***

### 📋 문법
```kotlin
map.putIfAbsent(key, value)
```

### 예제
```kotlin
fun main() {
    val map = mutableMapOf("apple" to 1)

    map.putIfAbsent("apple", 100)  // 이미 존재하므로 추가되지 않음
    map.putIfAbsent("banana", 200) // 존재하지 않으므로 추가됨

    println(map)  // 결과: {apple=1, banana=200}
}
```
### 사용 사례
1. 데이터베이스 캐싱
2. 키가 중복되지 않아야 할 때 사용
---


## ✅ 3 `getOrElse`

### 📌 설명
- **동작:** 키가 존재하면 값을 반환하고, 없으면 기본값을 반환 **(맵에 추가하지는 않음)**
- `getOrPut`과 달리 ***맵의 상태를 변경하지 않음***

### 📋 문법
```kotlin
map.getOrElse(key) { defaultValue }
```

### 예제
```kotlin
fun main() {
    val map = mapOf("apple" to 1)

    println(map.getOrElse("apple") { 100 })   // 출력: 1
    println(map.getOrElse("banana") { 200 })  // 출력: 200

    println(map)  // 결과: {apple=1} (변경 없음)
}
```
### 사용 사례
1. 읽기 전용 맵에서 기본값 처리할 때
2. 맵을 변경하지 않고 조회만 필요할 때
---


## ✅ 4 `getValue`

### 📌 설명
- **동작:** 키가 존재하면 값을 반환, 없으면 없으면 `NoSuchElementException 발생`
- 기본값 없이 **엄격한 조회**가 필요한 경우 사용

### 📋 문법
```kotlin
map.getValue(key)
```

### 예제
```kotlin
fun main() {
    val map = mapOf("apple" to 1)

    println(map.getValue("apple"))  // 출력: 1
    // println(map.getValue("banana"))  // ❌ 예외 발생: NoSuchElementException
}
```
### 사용 사례
1. 값이 반드시 존재해야 하는 경우
2. 실패 시 예외 처리를 통해 오류 감지

---


## ✅ 꼭 외워야 할 핵심 함수
### getOrPut → 값이 없으면 추가하면서 반환
### putIfAbsent → 값이 없을 때만 추가 (존재하면 무시)
### getOrElse → 기본값 반환 (맵 변경 없음)
### getValue → 반드시 존재하는 값 조회 (없으면 예외)
### set / put → 가장 기본적인 추가 및 수정

---

## 🚀 실제 사용 사례
### 1. 빈도수 세기
```kotlin
val words = listOf("apple", "banana", "apple", "orange")
val frequency = mutableMapOf<String, Int>()

for (word in words) {
    frequency[word] = frequency.getOrPut(word) { 0 } + 1
}

println(frequency)  // 결과: {apple=2, banana=1, orange=1}
```

### 2. 초기화된 리스트에 값 추가
```kotlin
val groups = mutableMapOf<String, MutableList<Int>>()

groups.getOrPut("Group A") { mutableListOf() }.add(1)
groups.getOrPut("Group A") { mutableListOf() }.add(2)
groups.getOrPut("Group B") { mutableListOf() }.add(3)

println(groups)  // 결과: {Group A=[1, 2], Group B=[3]}
```