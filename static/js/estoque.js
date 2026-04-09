const sidebar = document.querySelector(".sidebar");
const btn_sidebar_control = document.querySelector(".btn_sidebar_control");
btn_sidebar_control.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    btn_sidebar_control.classList.toggle("xs");
});
export {};
//# sourceMappingURL=estoque.js.map