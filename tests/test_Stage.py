import pytest
from fantasyCycling.model import Stage
from fantasyCycling.service.StageService import StageService

def test_that_stage_can_be_persisted():
    test_stage_service = StageService()
    test_stage = Stage("test_stage")
    test_stage_service.create_stage(test_stage)
    test_stage_id= test_stage_service.find_stage_by_name("test_stage")['_id']
    assert test_stage_service.find_stage_by_id(test_stage_id)['name'] == 'test_stage'
    
    


# @SpringBootTest
# @DirtiesContext(classMode = ClassMode.BEFORE_EACH_TEST_METHOD)
# class UserTest {

# 	@Autowired
# 	private UserService userService;
	
# 	@Autowired
# 	private StagePointsService stagePointsService;

# 	@Test
# 	void testThatAUserCanBePersisted() {
# 		User user = new User("Seb Brice", "brice", "abc123");
# 		userService.create(user);
# 		assertTrue(user.getUserId() > 0);

# 	}

# 	@Test
# 	void testThatAUserCanBeRetrieved() {
# 		User userFromDb = userService.retrieveOne(2).get();
# 		assertTrue(userFromDb instanceof User);
# 	}

# 	@Test
# 	void testThatAllUserCanBeRetrieved() {
# 		List<User> allUsers = userService.retrieveAll();
# 		assertFalse(allUsers.isEmpty());

# 	}

# 	@Test
# 	void testThatAUsersTotalStagePointsCanBeCalculated() {
# 		List<StagePoints> point = stagePointsService.getTeamStagePoints(1, 1);
# 		System.out.println(point);
# 		int score = userService.getTeamStageScore(1, 1);
# 		assertTrue(2011 == score);
# 	}

# 	@Test
# 	void testThatListOfUsersCyclistCanBeRetrieved() {
# 		List<Cyclist> team = userService.retrieveTeam(1);
# 		assertFalse(team.isEmpty());

# 	}
	
# 	@Test
# 	void test_thatCurrentStagePointsofUsercanbeCalculated() {
# 		int totalPoints = stagePointsService.getTotalCurrentPoints(1);
# 		assertTrue(totalPoints == 2011);
# 	}
	
# 	@Test
# 	void test_thatASubstitutionCanBeMade() {
# 		List<Cyclist> originalTeam = userService.retrieveTeam(1);
# 		userService.makeSubstitution(1, 2, 1);
# 		List<Cyclist> newTeam = userService.retrieveTeam(1);
# 		for (Cyclist cyclist : newTeam) {
# 			System.out.println(cyclist.getName()+"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
# 		}
# 		for (Cyclist cyclist : originalTeam) {
# 			System.out.println(cyclist.getName()+"======================================================================");
# 		}
# 		assertFalse(newTeam.get(7)==originalTeam.get(7), "Not changed riders");
		
# 	}

# }