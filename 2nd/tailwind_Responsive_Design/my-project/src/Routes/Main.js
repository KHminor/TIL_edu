import Menu from "./Menu"

function Main() {
  return(
    <div>
      <div className="w-11/12 mx-auto ">
        <nav className="grid grid-cols-2 gap-4 bg-orange-300 rounded-md h-20">
          <div className="">여긴 디브</div>
          <Menu />
        </nav>
      </div>
    </div>
  )
}
export default Main