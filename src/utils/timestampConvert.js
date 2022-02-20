export const timestampConvert = (timeStamp) => {
    let date = new Date(timeStamp);
    let year = date.getFullYear();
    let month = date.getMonth();
    let day = date.getDate();
    if (day < 10) {
        day = '0' + day;
    }
    if (month < 10) {
        month += 1;
        if (month !== 10) {
            month = '0' + month;
        }
    }
    return day + '/' + month + '/' + year
}
