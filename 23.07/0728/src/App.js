import MyComponent from './MyComponent';
import Sample from "./Sample"
import EventComponent from './EventComponent';

function App() {

  return (
    <>
      <MyComponent album = "genesis"/>
      <Sample album = "exodus">샘플 데이터</Sample>
      <EventComponent />
    </>
  );
}
export default App;
