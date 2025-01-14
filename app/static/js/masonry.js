// 初始化 Masonry 布局
function initMasonry() {
    const grid = document.querySelector('.row');
    if (grid) {
        new Masonry(grid, {
            itemSelector: '.col-md-4',
            percentPosition: true
        });
    }
}

// 在 DOM 加载完成后初始化 Masonry
document.addEventListener('DOMContentLoaded', function() {
    initMasonry();
});

// 如果 Vue 动态加载内容，可以在内容更新后重新初始化 Masonry
if (typeof Vue !== 'undefined') {
    Vue.createApp({
        mounted() {
            this.$nextTick(() => {
                initMasonry();
            });
        }
    });
}