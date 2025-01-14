document.addEventListener('DOMContentLoaded', function() {
    const { createApp, ref } = Vue;

    const app = createApp({
        setup() {
            // 获取当前日期
            const getCurrentDate = () => {
                const today = new Date();
                const year = today.getFullYear();
                const month = String(today.getMonth() + 1).padStart(2, '0'); // 月份从 0 开始，需要加 1
                const day = String(today.getDate()).padStart(2, '0');
                return `${year}-${month}-${day}`;
            };

            const newEntry = ref({
                date: getCurrentDate(),  // 默认日期为当天
                image: null,  // 用于存储文件对象
                description: ''
            });

            // 处理文件上传
            const handleImageUpload = (event) => {
                newEntry.value.image = event.target.files[0];  // 获取文件对象
            };

            // 添加点滴记录
            const addEntry = async () => {
                const formData = new FormData();
                formData.append('date', newEntry.value.date);
                formData.append('image', newEntry.value.image);
                formData.append('description', newEntry.value.description);

                const response = await fetch('/api/entries', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                alert(data.message); // 提示添加成功
                newEntry.value = { date: getCurrentDate(), image: null, description: '' }; // 清空表单
            };

            return {
                newEntry,
                handleImageUpload,
                addEntry
            };
        }
    });

    // 确保 #app 元素存在
    const mountElement = document.getElementById('app');
    if (mountElement) {
        app.mount('#app');
    } else {
        console.warn('Mount element (#app) not found.');
    }
});