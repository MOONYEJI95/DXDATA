// react.js 파일에서 export한 객체를 React로 받아서 사용
// {이름}의 경우는 export한 객체에서 이름에 해당하는 것만 받아서 사용
import react from "react"
import {
    ListItem,
    ListItemText,
    InputBase,
    Checkbox,
    ListItemSecondaryAction,
    IconButton
  } from "@material-ui/core";

//Icon 가져오기
import DeleteOutlined from "@material-ui/icons/DeleteOutlined";


class ToDo extends react.Component{
    //생성자
    constructor(props){
        super(props); // 상위 컴포넌트로부터 넘겨받은 데이터를 나의 props에 저장
        // props는 읽기 전용이라서 수정을 하고자 하는 경우
        // state에 복사해서 사용해야 함
        this.state = {item:props.item, readOnly:"true"}
        // this.state = {이름:초기값, 이름:초기값...}
        this.delete = props.delete;
        this.update = props.update;
    }
    // Event가 발생하면 readOnly의 값을 false로 수정
    offReadOnlyMode = (e) => {
        // state의 값을 직접 변경
        this.setState({readOnly:false})
    }
    // Enter를 눌렀을 때 동작하는 메서드
    enterKeyEventHandler = (e) => {
        if(e.key === "Enter"){
            this.setState({readOnly:true});
            // 데이터 수정
            this.update(this.state.item);
        }
    }

    // input의 내용을 변경했을 때 호출될 메서드
    editEventHandler = (e) => {
        const thisItem = this.state.item;
        thisItem.title = e.target.value;
        this.setState({item:thisItem});
        this.update(this.state.item);
    }

    // 체크박스의 값을 변경할 때 호출되는 메서드
    checkboxEventHandler = (e) => {
        const thisItem = this.state.item;
        thisItem.done = !thisItem.done;
        this.setState({item:thisItem});
        this.update(this.state.item);
    }


    // 삭제 아이콘을 눌렀을 때 호출될 함수
    deleteEventHandler = (e) => {
        this.delete(this.state.item);
    }





    render(){
        const item = this.state.item;
        return(
            <ListItem>
                <Checkbox checked={item.done} onChange={this.checkboxEventHandler}/>

                <ListItemText>
                    <InputBase
                        inputProps={{"aria-label" : "naked",
                    readOnly:this.state.readOnly}}
                        type="text"
                        id={item.id}
                        name={item.id}
                        value={item.title}
                        multiline={true}
                        fullwidth={true}
                        onClick={this.offReadOnlyMode}
                        onKeyPress={this.enterKeyEventHandler}
                        onChange={this.editEventHandler}
                    
                        />                  
                </ListItemText>

                <ListItemSecondaryAction>
                    <IconButton aria-label="Delete ToDo"
                    onClick={this.deleteEventHandler}>
                        <DeleteOutlined />
                    </IconButton>
                </ListItemSecondaryAction>
            </ListItem>
        )
    }
}
export default ToDo;
