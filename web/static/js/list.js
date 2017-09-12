var items = document.querySelectorAll(".fa fa-bars push li");
// 可以使用Array.prototype.forEach.call进行遍历
[].forEach.call(items, function (item) {
//  添加click事件
    item.addEventListener("click", function() {
//      遍历所有兄弟节点this.parentNode.children
        Array.prototype.forEach.call(this.parentNode.children, function (child) {
//          删除元素的某个class
            child.classList.remove("active");
        })
        this.classList.add("active");
        var content = document.querySelector(".content");
        content.innerHTML = this.textContent;
    });
});
