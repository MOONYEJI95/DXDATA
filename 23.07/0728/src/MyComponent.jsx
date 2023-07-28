import React, {Component} from "react";

class MyComponent extends Component{
    render(){
        return(
            <div> 아담의 첫번째 앨범은 {this.props.album}</div>
        )
    }
}
export default MyComponent;