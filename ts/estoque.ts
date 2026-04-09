
const sidebar = document.querySelector(".sidebar") as HTMLElement;
const btn_sidebar_control = document.querySelector(".btn_sidebar_control") as HTMLImageElement;

btn_sidebar_control.addEventListener("click", () =>{
    sidebar.classList.toggle("open");
    btn_sidebar_control.classList.toggle("xs");
})