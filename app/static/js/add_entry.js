const { createApp, ref } = Vue;

createApp({
    setup() {
        const newEntry = ref({
            date: '',
            image: '',
            description: ''
        });

        // 添加点滴记录
        const addEntry = async () => {
            const response = await fetch('/api/entries', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newEntry.value)
            });
            const data = await response.json();
            alert(data.message); // 提示添加成功
            newEntry.value = { date: '', image: '', description: '' }; // 清空表单
        };

        return {
            newEntry,
            addEntry
        };
    }
}).mount('#app');