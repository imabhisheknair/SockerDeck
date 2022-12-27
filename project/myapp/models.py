from django.db import models

#user_login, user_details, user_query, player_info, player_club_history, player_match_history, country_master, club_master, club_games

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user = models.ForeignKey(user_login, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    addr = models.CharField(max_length=1500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class country_master(models.Model):
    country = models.CharField(max_length=150)
    flag = models.CharField(max_length=150)
    budget= models.FloatField(default=2000000)

class club_master(models.Model):
    user = models.ForeignKey(user_login, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=150)
    c_descp = models.CharField(max_length=500)
    c_flag = models.CharField(max_length=250)
    addr = models.CharField(max_length=500)
    owner_details = models.CharField(max_length=150)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    remarks = models.CharField(max_length=350)
    url = models.CharField(max_length=250)


class user_query(models.Model):
    user = models.ForeignKey(user_login,  on_delete=models.CASCADE)
    age = models.CharField(max_length=150)
    height_cm = models.CharField(max_length=150)
    weight_kg = models.CharField(max_length=150)
    overall = models.CharField(max_length=150)
    player_positions = models.CharField(max_length=150)
    weak_foot = models.CharField(max_length=150)
    skill_moves = models.CharField(max_length=150)
    attacking_crossing = models.CharField(max_length=150)
    attacking_finishing = models.CharField(max_length=150)
    attacking_heading_accuracy = models.CharField(max_length=150)
    attacking_short_passing = models.CharField(max_length=150)
    attacking_volleys = models.CharField(max_length=150)
    skill_dribbling = models.CharField(max_length=150)
    skill_curve = models.CharField(max_length=150)
    skill_fk_accuracy = models.CharField(max_length=150)
    skill_long_passing = models.CharField(max_length=150)
    skill_ball_control = models.CharField(max_length=150)
    movement_acceleration = models.CharField(max_length=150)
    movement_sprint_speed = models.CharField(max_length=150)
    movement_agility = models.CharField(max_length=150)
    movement_reactions = models.CharField(max_length=150)
    movement_balance = models.CharField(max_length=150)
    power_shot_power = models.CharField(max_length=150)
    power_jumping = models.CharField(max_length=150)
    power_stamina = models.CharField(max_length=150)
    power_strength = models.CharField(max_length=150)
    power_long_shots = models.CharField(max_length=150)
    mentality_aggression = models.CharField(max_length=150)
    mentality_interceptions = models.CharField(max_length=150)
    mentality_positioning = models.CharField(max_length=150)
    mentality_vision = models.CharField(max_length=150)
    mentality_penalties = models.CharField(max_length=150)
    mentality_composure = models.CharField(max_length=150)
    defending_marking = models.CharField(max_length=150)
    defending_standing_tackle = models.CharField(max_length=150)
    defending_sliding_tackle = models.CharField(max_length=150)
    goalkeeping_diving = models.CharField(max_length=150)
    goalkeeping_handling = models.CharField(max_length=150)
    goalkeeping_kicking = models.CharField(max_length=150)
    goalkeeping_positioning = models.CharField(max_length=150)
    goalkeeping_reflexes = models.CharField(max_length=150)
    estimate = models.CharField(max_length=150)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)


class player_info(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    club = models.ForeignKey(club_master,  on_delete=models.CASCADE)
    country = models.ForeignKey(country_master,  on_delete=models.CASCADE)
    pic_path = models.CharField(max_length=250)
    descp = models.CharField(max_length=500)
    age = models.CharField(max_length=150)
    height_cm = models.CharField(max_length=150)
    weight_kg = models.CharField(max_length=150)
    overall = models.CharField(max_length=150)
    player_positions = models.CharField(max_length=150)
    weak_foot = models.CharField(max_length=150)
    skill_moves = models.CharField(max_length=150)
    attacking_crossing = models.CharField(max_length=150)
    attacking_finishing = models.CharField(max_length=150)
    attacking_heading_accuracy = models.CharField(max_length=150)
    attacking_short_passing = models.CharField(max_length=150)
    attacking_volleys = models.CharField(max_length=150)
    skill_dribbling = models.CharField(max_length=150)
    skill_curve = models.CharField(max_length=150)
    skill_fk_accuracy = models.CharField(max_length=150)
    skill_long_passing = models.CharField(max_length=150)
    skill_ball_control = models.CharField(max_length=150)
    movement_acceleration = models.CharField(max_length=150)
    movement_sprint_speed = models.CharField(max_length=150)
    movement_agility = models.CharField(max_length=150)
    movement_reactions = models.CharField(max_length=150)
    movement_balance = models.CharField(max_length=150)
    power_shot_power = models.CharField(max_length=150)
    power_jumping = models.CharField(max_length=150)
    power_stamina = models.CharField(max_length=150)
    power_strength = models.CharField(max_length=150)
    power_long_shots = models.CharField(max_length=150)
    mentality_aggression = models.CharField(max_length=150)
    mentality_interceptions = models.CharField(max_length=150)
    mentality_positioning = models.CharField(max_length=150)
    mentality_vision = models.CharField(max_length=150)
    mentality_penalties = models.CharField(max_length=150)
    mentality_composure = models.CharField(max_length=150)
    defending_marking = models.CharField(max_length=150)
    defending_standing_tackle = models.CharField(max_length=150)
    defending_sliding_tackle = models.CharField(max_length=150)
    goalkeeping_diving = models.CharField(max_length=150)
    goalkeeping_handling = models.CharField(max_length=150)
    goalkeeping_kicking = models.CharField(max_length=150)
    goalkeeping_positioning = models.CharField(max_length=150)
    goalkeeping_reflexes = models.CharField(max_length=150)
    estimate = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)

class player_club_history(models.Model):
    player = models.ForeignKey(player_info, on_delete=models.CASCADE)
    club = models.ForeignKey(club_master,  on_delete=models.CASCADE)
    fr_dt = models.CharField(max_length=50)
    to_dt = models.CharField(max_length=50)
    descp = models.CharField(max_length=550)
    curr_status = models.CharField(max_length=50)

class player_match_history(models.Model):
    player =  models.ForeignKey(player_info, on_delete=models.CASCADE)
    match_details = models.CharField(max_length=150)
    venue = models.CharField(max_length=350)
    player_team = models.CharField(max_length=150)
    player_no = models.CharField(max_length=15)
    opp_team = models.CharField(max_length=150)
    no_goals = models.IntegerField()
    descp = models.CharField(max_length=500)
    dt = models.CharField(max_length=150)

class club_games(models.Model):
    club = models.ForeignKey(club_master,  on_delete=models.CASCADE)
    game_name = models.CharField(max_length=150)
    game_sub_name = models.CharField(max_length=150)
    venue_details = models.CharField(max_length=350)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=150)
    result = models.CharField(max_length=150)

class club_player(models.Model):
    club = models.ForeignKey(club_master,  on_delete=models.CASCADE)
    player =  models.ForeignKey(player_info, on_delete=models.CASCADE)

class ClubRequests(models.Model):
    player = models.ForeignKey(player_info, on_delete=models.CASCADE)
    club = models.ForeignKey(club_master, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class PlayerRequests(models.Model):
    player = models.ForeignKey(player_info, on_delete=models.CASCADE)
    club = models.ForeignKey(club_master, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
