window.onload = function(){
		
	var data = {semester: "None", subject: "None", teacherName: "None", day: "None", roomNo: "None", timing: "None"};

	var dataTester = { 
		"8:30am-10:00am": "class-1",
		"10:15am-11:45am": "class-2",
		"12:00pm-1:30pm": "class-3",
		"2:00pm-3:30pm": "class-4",
	};


	var selectSemester = document.querySelector('form .semester');		
	selectSemester.addEventListener('change', semesterSelected);

	function semesterSelected(event){
		data.semester = event.target.value;		
	}	

	var pickSubject = document.querySelector('form .subject-name');
	pickSubject.addEventListener('change', subjectSelected);

	function subjectSelected(event){
		data.subject = event.target.value;
	}

	var teacherName = document.querySelector('form .teacher');
	teacherName.addEventListener('change', setTeacherName);

	function setTeacherName(event){
		data.teacherName = event.target.value;
	}

	var day = document.querySelector('form .day');
	day.addEventListener('change', setDay);

	function setDay(event){
		data.day = event.target.value;
	}

	var roomNo = document.querySelector('form .room-no');
	roomNo.addEventListener('change', setRoomNo);

	function setRoomNo(event){
		data.roomNo = event.target.value;
	}

	var timing = document.querySelector('form .timing');
	timing.addEventListener('change', setTiming);

	function setTiming(event){
		data.timing = event.target.value;
	}

	var addButton = document.querySelector('form .button');
	addButton.addEventListener('click', add);

	function add(event){
		var box = document.querySelector('.' + data.day + ' .' + dataTester[data.timing]);
		console.log('hey it is running');
		box.style.fontSize = '0.5em';
		box.style.color = '#fff';
		box.innerHTML = '<p>' + data.subject + '<br>' + data.roomNo + '<br>' + data.teacherName + '</p>';
	}
}

