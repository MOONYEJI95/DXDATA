function Sample(props){
    // 자바스크립트의 구조 분해 할당
    // =의 오른쪽에 객체를 설정하고
    // 왼쪽에서 {}안에 변수를 설정하면 변수 이름과 동일한 객체의 속성이
    // 분해되서 대입됨
    const {album, children} = props;

    return(<div>두 번째 앨범은 {album}
    태그 안의 내용은 {children}</div>)
}
export default Sample;