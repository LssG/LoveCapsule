document.addEventListener('DOMContentLoaded', function() {
    const { createApp, ref } = Vue;

    createApp({
        setup() {
            const newEntry = ref({
                date: '',
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
                newEntry.value = { date: '', image: null, description: '' }; // 清空表单
            };

            return {
                newEntry,
                handleImageUpload,
                addEntry
            };
        }
    }).mount('#app');
});