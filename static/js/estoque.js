const sidebar = document.querySelector(".sidebar");
const btn_sidebar_control = document.querySelector(".btn_sidebar_control");
const sidebar_login = document.querySelector(".sidebar_login");
btn_sidebar_control.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    btn_sidebar_control.classList.toggle("xs");
    sidebar_login.classList.toggle("sidebar_close");
});
export {};
//# sourceMappingURL=estoque.js.map