var 이미지 = document.querySelector('#image');
var 버튼 = document.querySelector('#btn');
if (버튼 instanceof HTMLButtonElement) {
    버튼.addEventListener('click', function () {
        if (이미지 instanceof HTMLImageElement) {
            이미지.src = 'new.jpg';
        }
    });
}
var 태그 = document.querySelectorAll('.naver');
태그.forEach(function (e) {
    if (e instanceof HTMLAnchorElement) {
        e.href = 'https://kakao.com';
    }
});
