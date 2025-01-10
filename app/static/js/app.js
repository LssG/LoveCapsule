const { createApp, ref, onMounted } = Vue;

createApp({
    setup() {
        const entries = ref([]);

        // 获取所有点滴记录
        const fetchEntries = async () => {
            const response = await fetch('/api/entries');
            const data = await response.json();
            entries.value = data;
        };

        // 删除点滴记录
        const deleteEntry = async (id) => {
            await fetch(`/api/entries/${id}`, {
                method: 'DELETE'
            });
            fetchEntries(); // 重新加载数据
        };

        // 组件挂载时加载数据
        onMounted(() => {
            fetchEntries();
        });

        return {
            entries,
            deleteEntry
        };
    }
}).mount('#app');