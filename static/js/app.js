new Vue({
    el: '#app',
    data: {
        capsules: []
    },
    mounted() {
        fetch('/api/capsules')
            .then(response => response.json())
            .then(data => {
                this.capsules = data;
            });
    }
});
