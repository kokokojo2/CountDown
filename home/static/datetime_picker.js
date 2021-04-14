var dateTimePicker = flatpickr("#id_finished",
            {
                dateFormat: "Y-m-d H:i:S",
                enableTime: true,
                time_24hr: true,
                enableSeconds: true,
                minuteIncrement: 1,
                disable: [
                    function(date) {
                        // return true to disable
                        var now = new Date;
                        now.setDate(now.getDate() - 1);
                        return (date <= now);
                    }
                ]
            });