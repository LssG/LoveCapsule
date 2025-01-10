document.addEventListener('DOMContentLoaded', function() {
    const app = new Vue({
        el: '#app',
        data: {
            entries: [],
            newEntry: {
                date: '',
                image: '',
                description: ''
            }
        },
        methods: {
            fetchEntries() {
                fetch('/api/entries')
                    .then(response => response.json())
                    .then(data => {
                        this.entries = data;
                    });
            },
            addEntry() {
                fetch('/api/entries', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.newEntry)
                })
                .then(response => response.json())
                .then(data => {
                    this.fetchEntries();
                    this.newEntry = { date: '', image: '', description: '' };
                });
            },
            deleteEntry(id) {
                fetch(`/api/entries/${id}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    this.fetchEntries();
                });
            }
        },
        mounted() {
            this.fetchEntries();
        }
    });
});