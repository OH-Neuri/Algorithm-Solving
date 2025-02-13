function solution(phone_book) {
  phone_book.sort(); // 전화번호 리스트를 정렬합니다.

  for (let i = 0; i < phone_book.length - 1; i++) {
    if (phone_book[i] === phone_book[i + 1].substring(0, phone_book[i].length)) {
      return false;
    }
  }

  return true;
}