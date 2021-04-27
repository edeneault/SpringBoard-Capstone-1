--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: athlete_workouts; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.athlete_workouts (
    id integer NOT NULL,
    rpe_avg integer,
    workout_date timestamp without time zone,
    workout_id integer,
    athlete_id integer
);


ALTER TABLE public.athlete_workouts OWNER TO edeneault;

--
-- Name: athlete_workouts_exercises; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.athlete_workouts_exercises (
    id integer NOT NULL,
    athlete_workout_id integer,
    workout_exercise_id integer
);


ALTER TABLE public.athlete_workouts_exercises OWNER TO edeneault;

--
-- Name: athlete_workouts_exercises_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.athlete_workouts_exercises_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.athlete_workouts_exercises_id_seq OWNER TO edeneault;

--
-- Name: athlete_workouts_exercises_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.athlete_workouts_exercises_id_seq OWNED BY public.athlete_workouts_exercises.id;


--
-- Name: athlete_workouts_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.athlete_workouts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.athlete_workouts_id_seq OWNER TO edeneault;

--
-- Name: athlete_workouts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.athlete_workouts_id_seq OWNED BY public.athlete_workouts.id;


--
-- Name: athletes; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.athletes (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(50),
    "position" character varying(30) NOT NULL,
    height integer,
    weight double precision,
    athlete_image_url text,
    medical_status text,
    created_on timestamp without time zone,
    team_id integer
);


ALTER TABLE public.athletes OWNER TO edeneault;

--
-- Name: athletes_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.athletes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.athletes_id_seq OWNER TO edeneault;

--
-- Name: athletes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.athletes_id_seq OWNED BY public.athletes.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    category_name character varying(20) NOT NULL
);


ALTER TABLE public.categories OWNER TO edeneault;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO edeneault;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: equipment; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.equipment (
    id integer NOT NULL,
    equipment_name character varying(50) NOT NULL
);


ALTER TABLE public.equipment OWNER TO edeneault;

--
-- Name: equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipment_id_seq OWNER TO edeneault;

--
-- Name: equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.equipment_id_seq OWNED BY public.equipment.id;


--
-- Name: exercises; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.exercises (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description text NOT NULL,
    default_reps integer,
    image_url text,
    wger_id integer,
    category_id integer,
    equipment_id integer,
    muscle_id integer
);


ALTER TABLE public.exercises OWNER TO edeneault;

--
-- Name: exercises_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.exercises_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_id_seq OWNER TO edeneault;

--
-- Name: exercises_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.exercises_id_seq OWNED BY public.exercises.id;


--
-- Name: images; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.images (
    id integer NOT NULL,
    exercise_image_url text NOT NULL,
    wger_id integer NOT NULL
);


ALTER TABLE public.images OWNER TO edeneault;

--
-- Name: images_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_id_seq OWNER TO edeneault;

--
-- Name: images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.images_id_seq OWNED BY public.images.id;


--
-- Name: muscles; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.muscles (
    id integer NOT NULL,
    muscle_name character varying(50) NOT NULL,
    image_url text
);


ALTER TABLE public.muscles OWNER TO edeneault;

--
-- Name: muscles_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.muscles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.muscles_id_seq OWNER TO edeneault;

--
-- Name: muscles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.muscles_id_seq OWNED BY public.muscles.id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.teams (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    location text NOT NULL,
    discipline text NOT NULL,
    team_image_url text,
    created_on timestamp without time zone,
    user_id integer
);


ALTER TABLE public.teams OWNER TO edeneault;

--
-- Name: teams_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teams_id_seq OWNER TO edeneault;

--
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.teams_id_seq OWNED BY public.teams.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    password text NOT NULL,
    email character varying(50) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    image_url text,
    header_image_url text,
    created_on timestamp without time zone NOT NULL
);


ALTER TABLE public.users OWNER TO edeneault;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO edeneault;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: workout_exercises; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.workout_exercises (
    id integer NOT NULL,
    workout_id integer,
    exercise_id integer
);


ALTER TABLE public.workout_exercises OWNER TO edeneault;

--
-- Name: workout_exercises_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.workout_exercises_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workout_exercises_id_seq OWNER TO edeneault;

--
-- Name: workout_exercises_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.workout_exercises_id_seq OWNED BY public.workout_exercises.id;


--
-- Name: workouts; Type: TABLE; Schema: public; Owner: edeneault
--

CREATE TABLE public.workouts (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.workouts OWNER TO edeneault;

--
-- Name: workouts_id_seq; Type: SEQUENCE; Schema: public; Owner: edeneault
--

CREATE SEQUENCE public.workouts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workouts_id_seq OWNER TO edeneault;

--
-- Name: workouts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edeneault
--

ALTER SEQUENCE public.workouts_id_seq OWNED BY public.workouts.id;


--
-- Name: athlete_workouts id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts ALTER COLUMN id SET DEFAULT nextval('public.athlete_workouts_id_seq'::regclass);


--
-- Name: athlete_workouts_exercises id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts_exercises ALTER COLUMN id SET DEFAULT nextval('public.athlete_workouts_exercises_id_seq'::regclass);


--
-- Name: athletes id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athletes ALTER COLUMN id SET DEFAULT nextval('public.athletes_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: equipment id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.equipment ALTER COLUMN id SET DEFAULT nextval('public.equipment_id_seq'::regclass);


--
-- Name: exercises id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.exercises ALTER COLUMN id SET DEFAULT nextval('public.exercises_id_seq'::regclass);


--
-- Name: images id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.images ALTER COLUMN id SET DEFAULT nextval('public.images_id_seq'::regclass);


--
-- Name: muscles id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.muscles ALTER COLUMN id SET DEFAULT nextval('public.muscles_id_seq'::regclass);


--
-- Name: teams id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.teams ALTER COLUMN id SET DEFAULT nextval('public.teams_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: workout_exercises id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workout_exercises ALTER COLUMN id SET DEFAULT nextval('public.workout_exercises_id_seq'::regclass);


--
-- Name: workouts id; Type: DEFAULT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workouts ALTER COLUMN id SET DEFAULT nextval('public.workouts_id_seq'::regclass);


--
-- Data for Name: athlete_workouts; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.athlete_workouts (id, rpe_avg, workout_date, workout_id, athlete_id) FROM stdin;
1	7	2021-04-27 00:00:00	1	1
2	7	2021-04-27 00:00:00	2	1
3	7	2021-04-27 00:00:00	2	2
4	7	2021-04-27 00:00:00	3	2
5	7	2021-04-27 00:00:00	4	3
6	7	2021-04-27 00:00:00	5	3
7	7	2021-04-27 00:00:00	6	4
8	7	2021-04-27 00:00:00	7	4
9	7	2021-04-27 00:00:00	8	10
10	7	2021-04-27 00:00:00	9	10
11	7	2021-04-27 00:00:00	1	12
12	7	2021-04-27 00:00:00	2	12
13	7	2021-04-27 00:00:00	2	24
14	7	2021-04-27 00:00:00	3	24
15	7	2021-04-27 00:00:00	4	34
16	7	2021-04-27 00:00:00	5	34
17	7	2021-04-27 00:00:00	7	16
18	7	2021-04-27 00:00:00	8	15
19	7	2021-04-27 00:00:00	6	16
20	7	2021-04-27 00:00:00	9	27
\.


--
-- Data for Name: athlete_workouts_exercises; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.athlete_workouts_exercises (id, athlete_workout_id, workout_exercise_id) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	4
5	5	5
6	6	6
7	7	7
8	8	8
9	9	9
10	10	10
11	11	11
12	12	12
13	13	13
14	14	14
15	15	15
16	16	16
17	17	17
18	18	18
19	19	19
20	20	20
\.


--
-- Data for Name: athletes; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.athletes (id, first_name, last_name, email, "position", height, weight, athlete_image_url, medical_status, created_on, team_id) FROM stdin;
1	Joe	Douglas	jdouglas@fakemail.com	Acro_Base	70	175	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
2	Peter	Johnson	pjohnson@fakegmail.com	Acro_Base	73	185	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
3	Lucille	Walker	lwalker@fakegmail.com	Acro_Flyer	57	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
4	Alexandra	Zumin	azumin@fakegmail.com	Acro_Flyer	58	100	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
5	John	Mgurk	jmagurk@fakegmail.com	Acro_Flyer	62	115	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
6	Alanna	FireStorm	afirestorm@fakegmail.com	Acro_Dancer	64	114	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	1
7	Sean	Soul	jsoul@fakemail.com	Full Stack	80	175	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
8	Jordan	Ash	jash@fakegmail.com	Front-End	73	185	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
9	Joshua	Lewis	jlewisr@fakegmail.com	Back-end	57	135	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
10	Mack	Prairie	mprairie@fakegmail.com	Database Admin	76	170	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
11	Pierre	Loyette	ployette@fakegmail.com	UX-UI Designer	78	165	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
12	Mike	Jordan	mjordan@fakegmail.com	Project Manager	77	230	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	2
13	Kayla	Lau	klow@fakemail.com	Tramp Wall	70	155	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
14	Sam	Lake	slake@fakegmail.com	Acro-Character	73	125	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
15	Alex	Men	amen@fakegmail.com	Aerialist	57	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
16	Julia	More	jmore@fakegmail.com	Aerialist	58	100	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
17	Janette	Pow	jpow@fakegmail.com	Trapeze Flyer	62	115	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
18	Anna	Kilt	akilt@fakegmail.com	Power Track	64	114	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	3
19	Emma	Lau	elau@fakemail.com	Road cyclist	70	155	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
20	Zoe	Lake	zlake@fakegmail.com	Road cyclist	73	125	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
21	Lisa	Men	lmen@fakegmail.com	Road cyclist	57	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
22	Philip	More	lmore@fakegmail.com	Road cyclist	58	100	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
23	Vincent	Pow	vpow@fakegmail.com	Road cyclist	62	115	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
24	Anatoli	Kilt	aakilt@fakegmail.com	Road cyclist	64	114	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	4
25	Qiqi	La	qla@fakemail.com	Rhytmic Gymnast	70	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
26	Virginia	Lake	vlake@fakegmail.com	Rhytmic Gymnast	73	90.5	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
27	Victoria	Men	vmen@fakegmail.com	Rhytmic Gymnast	57	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
28	Marie	More	mmore@fakegmail.com	Rhytmic Gymnast	58	100.2	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
29	Ella	Pow	epow@fakegmail.com	Rhytmic Gymnast	62	105.5	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
30	Melanie	Kilt	mkilt@fakegmail.com	Rhytmic Gymnast	64	97	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	5
31	Laura	La	qla@fakemail.com	Rhytmic Gymnast	70	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
32	Louanne	Lake	vlake@fakegmail.com	Rhytmic Gymnast	73	90.5	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
33	Lexa	Men	vmen@fakegmail.com	Rhytmic Gymnast	57	95	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
34	Belle	More	mmore@fakegmail.com	Rhytmic Gymnast	58	100.2	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
35	Maya	Pow	epow@fakegmail.com	Rhytmic Gymnast	62	105.5	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
36	Olga	Kilt	okilt@fakegmail.com	Rhytmic Gymnast	64	97	/static/images/default-pic.png	Full Duty	2021-04-27 00:00:00	6
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.categories (id, category_name) FROM stdin;
1	Abs
2	Arms
3	Back
4	Calves
5	Chest
6	Legs
7	Shoulders
\.


--
-- Data for Name: equipment; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.equipment (id, equipment_name) FROM stdin;
1	Barbell
2	Bench
3	Dumbbell
4	Gym mat
5	Incline bench
6	Kettlebell
7	none (bodyweight exercise)
8	Pull-up bar
9	Swiss Ball
10	SZ-Bar
\.


--
-- Data for Name: exercises; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.exercises (id, name, description, default_reps, image_url, wger_id, category_id, equipment_id, muscle_id) FROM stdin;
1	flat bench press	On you bench press rack of choice, set-up in flat configuration, use a barbell to press up and down, make sure to have a spotter.	7	/static/images/default-pic.png	192	5	1	1
2	Air Squat	Perform a squat with no resistance, make sure stance is slightly wider then shoulder width and feet are turned out.	7	/static/images/default-pic.png	111	6	7	2
3	push up	Assume a support position, perform a push up, make sure to engage your core while performing each repetition.	7	/static/images/default-pic.png	182	5	7	1
4	crunches	Sit and lay back on a swiss ball, position feet slightly wider then shoulder width, perform a half-crunch fully engaging the core.	7	/static/images/default-pic.png	91	1	9	3
5	concentration curl	Using dumbells, sit on a bench, one arm at a time, position your arm against your leg and perform a curl.	7	/static/images/default-pic.png	74	2	3	4
6	2 Handed Kettlebell Swing	<p>Two Handed Russian Style Kettlebell swing</p>	7	/static/images/default-pic.png	345	1	6	1
7	Arnold Shoulder Press	<p>Very common shoulder exercise.</p>\n<p> </p>\n<p>As shown here: https://www.youtube.com/watch?v=vj2w851ZHRM</p>	7	/static/images/default-pic.png	227	7	3	1
8	Axe Hold	<p>Grab dumbbells and extend arms to side and hold as long as you can</p>	7	/static/images/default-pic.png	289	2	3	1
9	Back Squat	<p>Place a barbell in a rack just below shoulder-height. Dip under the bar to put it behind the neck across the top of the back, and grip the bar with the hands wider than shoulder-width apart. Lift the chest up and squeeze the shoulder blades together to keep the straight back throughout the entire movement. Stand up to bring the bar off the rack and step backwards, then place the feet so that they are a little wider than shoulder-width apart. Sit back into hips and keep the back straight and the chest up, squatting down so the hips are below the knees. From the bottom of the squat, press feet into the ground and push hips forward to return to the top of the standing position.</p>	7	/static/images/default-pic.png	637	6	1	1
10	Barbell Ab Rollout	<p>Place a barbell on the floor at your feet.</p>\n<p>Bending at the waist, grip the barbell with a shoulder with overhand grip.</p>\n<p>With a slow controlled motion, roll the bar out so that your back is straight.</p>\n<p>Roll back up raising your hips and butt as you return to the starting position.</p>	7	/static/images/default-pic.png	343	1	1	8
11	2 Handed Kettlebell Swing	<p>Two Handed Russian Style Kettlebell swing</p>	7	/static/images/default-pic.png	345	1	6	1
12	Arnold Shoulder Press	<p>Very common shoulder exercise.</p>\n<p> </p>\n<p>As shown here: https://www.youtube.com/watch?v=vj2w851ZHRM</p>	7	/static/images/default-pic.png	227	7	3	1
13	Axe Hold	<p>Grab dumbbells and extend arms to side and hold as long as you can</p>	7	/static/images/default-pic.png	289	2	3	1
14	Back Squat	<p>Place a barbell in a rack just below shoulder-height. Dip under the bar to put it behind the neck across the top of the back, and grip the bar with the hands wider than shoulder-width apart. Lift the chest up and squeeze the shoulder blades together to keep the straight back throughout the entire movement. Stand up to bring the bar off the rack and step backwards, then place the feet so that they are a little wider than shoulder-width apart. Sit back into hips and keep the back straight and the chest up, squatting down so the hips are below the knees. From the bottom of the squat, press feet into the ground and push hips forward to return to the top of the standing position.</p>	7	/static/images/default-pic.png	637	6	1	1
15	Barbell Ab Rollout	<p>Place a barbell on the floor at your feet.</p>\n<p>Bending at the waist, grip the barbell with a shoulder with overhand grip.</p>\n<p>With a slow controlled motion, roll the bar out so that your back is straight.</p>\n<p>Roll back up raising your hips and butt as you return to the starting position.</p>	7	/static/images/default-pic.png	343	1	1	8
16	2 Handed Kettlebell Swing	<p>Two Handed Russian Style Kettlebell swing</p>	7	/static/images/default-pic.png	345	1	6	1
17	Arnold Shoulder Press	<p>Very common shoulder exercise.</p>\n<p> </p>\n<p>As shown here: https://www.youtube.com/watch?v=vj2w851ZHRM</p>	7	/static/images/default-pic.png	227	7	3	1
18	Axe Hold	<p>Grab dumbbells and extend arms to side and hold as long as you can</p>	7	/static/images/default-pic.png	289	2	3	1
19	Back Squat	<p>Place a barbell in a rack just below shoulder-height. Dip under the bar to put it behind the neck across the top of the back, and grip the bar with the hands wider than shoulder-width apart. Lift the chest up and squeeze the shoulder blades together to keep the straight back throughout the entire movement. Stand up to bring the bar off the rack and step backwards, then place the feet so that they are a little wider than shoulder-width apart. Sit back into hips and keep the back straight and the chest up, squatting down so the hips are below the knees. From the bottom of the squat, press feet into the ground and push hips forward to return to the top of the standing position.</p>	7	/static/images/default-pic.png	637	6	1	1
20	Barbell Ab Rollout	<p>Place a barbell on the floor at your feet.</p>\n<p>Bending at the waist, grip the barbell with a shoulder with overhand grip.</p>\n<p>With a slow controlled motion, roll the bar out so that your back is straight.</p>\n<p>Roll back up raising your hips and butt as you return to the starting position.</p>	7	/static/images/default-pic.png	343	1	1	8
21	Barbell Hack Squats	<p>Perform leg squats with barbell behind your legs</p>	7	/static/images/default-pic.png	407	6	1	10
22	Barbell Lunges	<p>Put barbell on the back of your shoulders. Stand upright, then take the first step forward. Step should bring you forward so that your supporting legs knee can touch the floor. Then stand back up and repeat with the other leg.</p>\n<p>Remember to keep good posture.</p>	7	/static/images/default-pic.png	405	6	1	10
23	Barbell Triceps Extension	<p>Position barbell overhead with narrow overhand grip.</p>\n<p>Lower forearm behind upper arm with elbows remaining overhead. Extend forearm overhead. Lower and repeat.</p>	7	/static/images/default-pic.png	344	2	1	15
24	Bear Walk	<p>-Rest your weight on your palms and the balls of your feet, not dissimilar to normal pushup position</p>\n<p>-Move by stepping with your R palm and L foot, then your L palm and R foot.  Basically, walk like a lumbering bear.</p>\n<p>-Move as fast as you can.  Measure your reps/sets in either distance (i.e. 40 yards) or time (i.e. 45 seconds)</p>\n<p>-Works your Pecs, Deltoids, Triceps, Traps, Lats, Abs and Lower Back, Hip Flexors, Quads, Glutes and Calves</p>	7	/static/images/default-pic.png	307	5	7	1
64	Curl su Panca a 45°	<p>Bicipiti su panca a 45°. Il movimento deve essere completo</p>	7	/static/images/default-pic.png	619	2	2	2
93	Front Squats	<p>Squats</p>	7	/static/images/default-pic.png	191	6	1	6
25	Bench Press	<p>Lay down on a bench, the bar should be directly above your eyes, the knees are somewhat angled and the feet are firmly on the floor. Concentrate, breath deeply and grab the bar more than shoulder wide. Bring it slowly down till it briefly touches your chest at the height of your nipples. Push the bar up.</p>\n<p>If you train with a high weight it is advisable to have a <em>spotter</em> that can help you up if you can't lift the weight on your own.</p>\n<p>With the width of the grip you can also control which part of the chest is trained more:</p>\n<ul>\n<li>wide grip: outer chest muscles</li>\n<li>narrow grip: inner chest muscles and triceps</li>\n</ul>	7	/static/images/default-pic.png	192	5	1	9
26	Benchpress Dumbbells	<p>The movement is very similar to benchpressing with a barbell, however, the weight is brought down to the chest at a lower point.</p>\n<p>Hold two dumbbells and lay down on a bench. Hold the weights next to the chest, at the height of your nipples and press them up till the arms are stretched. Let the weight slowly and controlled down.</p>	7	/static/images/default-pic.png	97	5	2	9
27	Bench Press Narrow Grip	<p>Lay down on a bench, the bar is directly over your eyes, the knees form a slight angle and the feet are firmly on the ground. Hold the bar with a narrow grip (around 20cm.). Lead the weight slowly down till the arms are parallel to the floor (elbow: right angle), press then the bar up. When bringing the bar down, don't let it down on your nipples as with the regular bench pressing, but somewhat lower.</p>	7	/static/images/default-pic.png	88	2	1	15
28	Bent High Pulls	<p>Bend over slightly while holding two dumbbells.  Pull the dumbbells up to your chest, keeping your elbows as high as you can.</p>	7	/static/images/default-pic.png	268	7	3	14
29	Bent Over Barbell Row	<ol>\n<li>Holding a barbell with a pronated grip (palms facing down), bend your knees slightly and bring your torso forward, by bending at the waist, while keeping the back straight until it is almost parallel to the floor. Tip: Make sure that you keep the head up. The barbell should hang directly in front of you as your arms hang perpendicular to the floor and your torso. This is your starting position.</li>\n<li>Now, while keeping the torso stationary, breathe out and lift the barbell to you. Keep the elbows close to the body and only use the forearms to hold the weight. At the top contracted position, squeeze the back muscles and hold for a brief pause.</li>\n<li>Then inhale and slowly lower the barbell back to the starting position.</li>\n<li>Repeat for the recommended amount of repetitions.</li>\n</ol>	7	/static/images/default-pic.png	412	3	1	1
30	Bentover Dumbbell Rows	<p>With dumbbells in hand, bend at the hip until hands hang just below the knees (similar to straight-legged-deadlift starting position). Keep upper body angle constant while contracting your lats to pull you ellbows back pinching the shoulder blades at the top. Try not to stand up with every rep, check hands go below knees on every rep.</p>	7	/static/images/default-pic.png	362	3	3	7
31	Bent-over Lateral Raises	<p>Sit on bench while holding weights. Bend forward as far as possible, with arms slightly bent at the elbow. Perform a lateral raise while maintaining the bend in your elbow.</p>	7	/static/images/default-pic.png	421	7	2	1
32	Bent Over Rowing	<p>Grab the barbell with a wide grip (slightly more than shoulder wide) and lean forward. Your upper body is not quite parallel to the floor, but forms a slight angle. The chest's out during the whole exercise.</p>\n<p>Pull now the barbell with a fast movement towards your belly button, not further up. Go slowly down to the initial position. Don't swing with your body and keep your arms next to your body.</p>	7	/static/images/default-pic.png	109	3	1	7
33	Bent Over Rowing Reverse	<p>The same as <em>regular</em> rowing, but holding a reversed grip (your palms pointing forwards):</p>\n<p>Grab the barbell with a wide grIp (slightly more than shoulder wide) and lean forward. Your upper body is not quite parallel to the floor, but forms a slight angle. The chest's out during the whole exercise.</p>\n<p>Pull now the barbell with a fast movement towards your belly button, not further up. Go slowly down to the initial position. Don't swing with your body and keep your arms next to your body.</p>	7	/static/images/default-pic.png	110	3	1	7
34	Biceps Curls With Barbell	<p>Hold the Barbell shoulder-wide, the back is straight, the shoulders slightly back, the arms are streched. Bend the arms, bringing the weight up, with a fast movement. Without pausing, let down the bar with a slow and controlled movement.</p>\n<p>Don't allow your body to swing during the exercise, all work is done by the biceps, which are the only mucles that should move (pay attention to the elbows).</p>	7	/static/images/default-pic.png	74	2	1	2
35	Biceps Curls With Dumbbell	<p>Hold two barbells, the arms are streched, the hands are on your side, the palms face inwards. Bend the arms and bring the weight with a fast movement up. At the same time, rotate your arms by 90 degrees at the very beginning of the movement. At the highest point, rotate a little the weights further outwards. Without a pause, bring them down, slowly.</p>\n<p>Don't allow your body to swing during the exercise, all work is done by the biceps, which are the only mucles that should move (pay attention to the elbows).</p>	7	/static/images/default-pic.png	81	2	3	2
36	Biceps Curls With SZ-bar	<p>Hold the SZ-bar shoulder-wide, the back is straight, the shoulders slightly back, the arms are streched. Bend the arms, bringing the weight up, with a fast movement. Without pausing, let down the bar with a slow and controlled movement.</p>\n<p>Don't allow your body to swing during the exercise, all work is done by the biceps, which are the only mucles that should move (pay attention to the elbows).</p>	7	/static/images/default-pic.png	80	2	10	2
37	Biceps Curl With Cable	<p>Stand around 30 - 40cm away from the cable, the feet are firmly on the floor. Take the bar and lift the weight with a fast movements. Lower the weight as with the dumbbell curls slowly and controlled.</p>	7	/static/images/default-pic.png	129	2	1	2
38	Body-Ups	<ol>\n<li>Assume a plank position on the ground. You should be supporting your bodyweight on your toes and forearms, keeping your torso straight. Your forearms should be shoulder-width apart. This will be your starting position.</li>\n<li>Pressing your palms firmly into the ground, extend through the elbows to raise your body from the ground. Keep your torso rigid as you perform the movement.</li>\n<li>Slowly lower your forearms back to the ground by allowing the elbows to flex.</li>\n<li>Repeat as needed.</li>\n</ol>	7	/static/images/default-pic.png	341	2	7	15
39	Braced Squat	<p>Stand with feet slightly wider than shoulder-width apart, while standing as tall as you can.</p>\n<p>Grab a weight plate and hold it out in front of your body with arms straight out. Keep your core tight and stand with a natural arch in your back.</p>\n<p>Now, push hips back and bend knees down into a squat as far as you can. Hold for a few moments and bring yourself back up to the starting position.</p>	7	/static/images/default-pic.png	342	6	1	10
40	Burpees	<p>Jump, lay down on your chest, do a pushup then jump, repeat</p>	7	/static/images/default-pic.png	354	5	1	1
41	Butterfly	<p>Sit on the butterfly machine, the feet have a good contact with the floor, the upper arms are parallel to the floor. Press your arms together till the handles are practically together (but aren't!). Go slowly back. The weights should stay all the time in the air.</p>	7	/static/images/default-pic.png	98	5	1	9
42	Butterfly Narrow Grip	<p>The movement is the same as with a regular butterfly, only that the grip is narrow:</p>\n<p>Sit on the butterfly machine, the feet have a good contact with the floor, the upper arms are parallel to the floor. Press your arms together till the handles are practically together (but aren't!). Go slowly back. The weights should stay all the time in the air.</p>	7	/static/images/default-pic.png	99	5	1	9
43	Butterfly Reverse		7	/static/images/default-pic.png	124	7	1	1
44	Cable Cross-over	<p>Begin with cables at about shoulder height, one in each hand. Take a step forward so that one foot is in front of the other, for stability, and so that there is tension on the cables. Bring hands together in front of you. Try to make your hands overlap (so that the cables cross) a few inches.</p>	7	/static/images/default-pic.png	207	5	1	9
45	Cable External Rotation	<p>Steps:</p>\n<ol>\n<li>Start off placing an extension band around a post or in a secure position where it will not release and is at elbow level.</li>\n<li>Position yourself to the side of the band and with your hand that is opposite of the band, reach out and grab the handle.</li>\n<li>Bring the band to your chest keeping your elbow bent in a 90 degree angle then slowly rotate your arm in a backhand motion so that the band externally rotates out</li>\n<li>Continue out as far as possible so that you feel a stretch in your shoulders, hold for a count and then return back to the starting position.</li>\n<li>Repeat for as many reps and sets as desired.</li>\n</ol>	7	/static/images/default-pic.png	265	7	1	1
46	Cable Woodchoppers	<p>Set cable pulley slightly lower than chest height. Keep body facing forward with hips stable.  Grab the pulley handle, fully extend your arms and bring your arms forward and across your body. Hold for 1 second at the end of the movement and slowly return to starting position.</p>	7	/static/images/default-pic.png	167	1	1	8
47	Calf Press Using Leg Press Machine	<p>Put  the balls of your feet on an extended leg press pad.  Use your calves to press the weight by flexing your feet/toes into a pointed position, and releasing back into a relaxed position.</p>\n<p>This exercise builds mass and strength in the Gastrocnemius and Soleus muscles as well, if not better, than any calf exercise.</p>	7	/static/images/default-pic.png	308	4	1	5
48	Calf Raises	Calf raises are a method of exercising the gastrocnemius, tibialis posterior and soleus muscles of the lower leg. The movement performed is plantar flexion, a.k.a. ankle extension.	7	/static/images/default-pic.png	776	4	3	5
49	Calf Raises on Hackenschmitt Machine	<p>Place yourself on the machine with your back firmly against the backrest, the feet are on the platform for calf raises. Check that the feet are half free and that you can completely stretch the calf muscles down.</p>\n<p>With straight knees pull up your weight as much as you can. Go with a fluid movement down till the calves are completely stretched. Repeat.</p>	7	/static/images/default-pic.png	104	4	1	5
50	Chin Up	The chin-up (also known as a chin or chinup) is a strength training exercise. People frequently do this exercise with the intention of strengthening muscles such as the latissimus dorsi and biceps, which extend the shoulder and flex the elbow, respectively. In this maneuver, the palms are faced towards the body. It is a form of pull-up in which the range of motion is established in relation to a person's chin.	7	/static/images/default-pic.png	803	3	8	2
51	Chin-ups	<p>Like pull-ups but with a reverse grip</p>	7	/static/images/default-pic.png	181	3	8	2
52	Close-grip Bench Press	<p>Perform a typical bench press, but hold the bar with your hands approximately shoulder-width apart and keep your elbows close to your body.</p>	7	/static/images/default-pic.png	217	2	1	15
53	Close-grip Lat Pull Down	<p>Grip the pull-down bar with your hands closer than shoulder width apart, with your palms facing away from you. Lean back slightly. Pull the bar down towards your chest, keeping your elbows close to your sides as you come down. Pull your shoulders back at the end of the motion.</p>	7	/static/images/default-pic.png	213	3	1	7
54	Cross-Bench Dumbbell Pullovers	<p>Grasp a moderately weighted dumbbell so your palms are flat against the underside of the top plates and your thumbs are around the bar. Lie on your back across a flat bench so only your upper back and shoulders are in contact with the bench. Your feet should be set about shoulder-width apart and your head should hang slightly downward. With the dumbbell supported at arm's length directly about your chest, bend your arms about 15 degrees and keep them bent throughout the movement. Slowly lower the dumbbell backward and downward in a semicircle arc to as low a position as is comfortably possible. Raise it slowly back along the same arc to the starting point, and repeat for the required number of repetitions.</p>	7	/static/images/default-pic.png	194	5	1	7
55	Crunches	<p>Lay down on your back a soft surface, the feet are on the floor. Ask a partner or use some other help (barbell, etc.) to keep them fixed, your hands are behind your head. From this position move your upper body up till your head or elbows touch your knees. Do this movement by rolling up your back.</p>	7	/static/images/default-pic.png	91	1	2	11
56	Chin-ups	<p>Like pull-ups but with a reverse grip</p>	7	/static/images/default-pic.png	181	3	8	2
57	Close-grip Bench Press	<p>Perform a typical bench press, but hold the bar with your hands approximately shoulder-width apart and keep your elbows close to your body.</p>	7	/static/images/default-pic.png	217	2	1	15
58	Close-grip Lat Pull Down	<p>Grip the pull-down bar with your hands closer than shoulder width apart, with your palms facing away from you. Lean back slightly. Pull the bar down towards your chest, keeping your elbows close to your sides as you come down. Pull your shoulders back at the end of the motion.</p>	7	/static/images/default-pic.png	213	3	1	7
59	Cross-Bench Dumbbell Pullovers	<p>Grasp a moderately weighted dumbbell so your palms are flat against the underside of the top plates and your thumbs are around the bar. Lie on your back across a flat bench so only your upper back and shoulders are in contact with the bench. Your feet should be set about shoulder-width apart and your head should hang slightly downward. With the dumbbell supported at arm's length directly about your chest, bend your arms about 15 degrees and keep them bent throughout the movement. Slowly lower the dumbbell backward and downward in a semicircle arc to as low a position as is comfortably possible. Raise it slowly back along the same arc to the starting point, and repeat for the required number of repetitions.</p>	7	/static/images/default-pic.png	194	5	1	7
87	Fly With Cable		7	/static/images/default-pic.png	122	5	1	9
60	Crunches	<p>Lay down on your back a soft surface, the feet are on the floor. Ask a partner or use some other help (barbell, etc.) to keep them fixed, your hands are behind your head. From this position move your upper body up till your head or elbows touch your knees. Do this movement by rolling up your back.</p>	7	/static/images/default-pic.png	91	1	2	11
61	Crunches on Machine	<p>The procedure is very similar as for regular crunches, only with the additional weight of the machine. Sit on the machine, put both feet firmly on the ground. Grab the to the weights, cables, etc. and do a rolling motion forwards (the spine should ideally lose touch vertebra by vertebra). Slowly return to the starting position. </p>	7	/static/images/default-pic.png	94	1	1	11
62	Crunches With Cable	<p>Take the cable on your hands and hold it next to your temples. Knee down and hold your upper body straight and bend forward. Go down with a fast movement, rolling your back in (your ellbows point to your knees). Once down, go slowly back to the initial position.</p>	7	/static/images/default-pic.png	92	1	1	11
63	Crunches With Legs Up	<p>On your back, legs extended straight up, reach toward your toes with your hands and lift your shoulder blades off the ground and back.</p>	7	/static/images/default-pic.png	416	1	1	11
65	Cycling	Cycling, also called bicycling or biking, is the use of bicycles for transport, recreation, exercise or sport. People engaged in cycling are referred to as cyclists, bicyclists, or bikers. Apart from two-wheeled bicycles, cycling also includes the riding of unicycles, tricycles, quadracycles, recumbent and similar human-powered vehicles.	7	/static/images/default-pic.png	806	6	7	8
67	Deadhang	<p>Deadhang performed on an edge either with or without added weight (adujst edge or weight to adjust difficulty)</p>	7	/static/images/default-pic.png	347	2	1	1
68	Deadlifts	<p>Stand firmly, with your feet slightly more than shoulder wide apart. Stand directly behind the bar where it should barely touch your shin, your feet pointing a bit out. Bend down with a straight back, the knees also pointing somewhat out. Grab the bar with a shoulder wide grip, one underhand, one reverse grip.</p>\n<p>Pull the weight up. At the highest point make a slight hollow back and pull the bar back. Hold 1 or 2 seconds that position. Go down, making sure the back is not bent. Once down you can either go back again as soon as the weights touch the floor, or make a pause, depending on the weight.</p>	7	/static/images/default-pic.png	105	3	1	7
69	Decline Bench Press Barbell	<p>Lay down on a decline bench, the bar should be directly above your eyes, the knees are somewhat angled and the feet are firmly on the floor. Concentrate, breath deeply and grab the bar more than shoulder wide. Bring it slowly down till it briefly touches your chest at the height of your nipples. Push the bar up.</p>	7	/static/images/default-pic.png	100	5	1	9
71	Decline Pushups	<p>With your feet raised approximately 30cm on a platform, align your shoulders, elbows and hands, then perform regular pushups. This emphasises the clavicular fibers of the pectoralis major.</p>	7	/static/images/default-pic.png	260	5	7	9
73	Diagonal Shoulder Press	<p>You sit at the bench press device, back slightly tilted to the back. The bar should be about 20 cm in front of you. Then you push the bar and take it back again, as you would with a bench press.</p>\n<p>In this position you strain your chest muscles a lot less, which is nice if you want to train, but your chest hasn't recovered yet.</p>\n<p>Here's a link to a girl on a machine specialized for this exercise, to give a better description than my failing words above.</p>\n<p>http://www.schnell-online.de/db_imgs/products/img/t-80400.jpg</p>	7	/static/images/default-pic.png	329	7	2	1
74	Dips	A dip is an upper-body strength exercise. Narrow, shoulder-width dips primarily train the triceps, with major synergists being the anterior deltoid, the pectoralis muscles (sternal, clavicular, and minor), and the rhomboid muscles of the back (in that order).[1] Wide arm training places additional emphasis on the pectoral muscles, similar in respect to the way a wide grip bench press would focus more on the pectorals and less on the triceps.	7	/static/images/default-pic.png	781	5	7	9
75	Dips	<p>Hold onto the bars at a narrow place (if they are not parallel) and press yourself up, but don't stretch the arms completely, so the muscles stay during the whole exercise under tension. Now bend the arms and go down as much as you can, keeping the elbows always pointing back, At this point, you can make a short pause before repeating the movement.</p>	7	/static/images/default-pic.png	82	2	1	15
76	Dips Between Two Benches	<p>Put two benches so far appart, that you can hold onto one with your hands and are just able to reach the other with your feet. The legs stay during the exercise completely stretched. With your elbows facing back, bend them as much as you can. Push yourself up, but don't stretch out the arms.</p>	7	/static/images/default-pic.png	83	2	2	15
77	Dumbbell Concentration Curl	<p>Sit on bench. Grasp dumbbell between feet. Place back of upper arm to inner thigh. Lean into leg to raise elbow slightly.</p>	7	/static/images/default-pic.png	275	2	3	4
79	Dumbbell Incline Curl	<p>With elbows back to sides, raise one dumbbell and rotate forearm until forearm is vertical and palm faces shoulder. Lower to original position and repeat with opposite arm. Continue to alternate between sides.</p>	7	/static/images/default-pic.png	298	2	3	2
80	Dumbbell Lunges Standing	<p>.</p>	7	/static/images/default-pic.png	112	6	3	10
81	Dumbbell Lunges Walking	<p>Take two dumbbells in your hands, stand straight, feet about shoulder wide. Take one long step so that the front knee is approximately forming a right angle. The back leg is streched, the knee is low but doesn't touch the ground. "Complete" the step by standing up and repeat the movement with the other leg.</p>	7	/static/images/default-pic.png	113	6	3	10
82	Dumbbells on Scott Machine		7	/static/images/default-pic.png	87	2	1	2
83	Dumbbell Triceps Extension	<p>Position one dumbbell over head with both hands under inner plate (heart shaped grip).</p>\n<p>With elbows over head, lower forearm behind upper arm by flexing elbows. Flex wrists at bottom to avoid hitting dumbbell on back of neck. Raise dumbbell over head by extending elbows while hyperextending wrists. Return and repeat.</p>	7	/static/images/default-pic.png	274	2	3	15
85	Facepull	<p>Attach a rope to a pulley station set at about chest level.</p>\n<p>Step back so you're supporting the weight with arms completely outstretched and assume a staggered (one foot forward) stance. Bend the knees slightly for a stable base.</p>\n<p>Retract the scapulae (squeeze your partner's finger with your shoulder blades) and pull the center of the rope slightly up towards the face. A good cue is to think about pulling the ends of the rope apart, not just pulling back.</p>\n<p>As you near your face, externally rotate so your knuckles are facing the ceiling.</p>\n<p>Hold for one second at the top position and slowly lower.</p>	7	/static/images/default-pic.png	394	7	1	14
66	Deadbug	Lie on your back, with your hips and knees bent to 90°. Raise both arms toward the ceiling. Pull your lower back to the floor to eliminate the gap. Start by pressing one leg out, and tapping the heel to the floor. "As you extend one leg, exhale as much as you can, keeping your lower back glued to the floor," Dunham says. When you can’t exhale any more, pull your knee back to the starting position. Make this more difficult by holding weight in your hands, or by lowering opposite arm and leg.	7	/static/images/default-pic.png	544	1	1	1
70	Decline Bench Press Dumbbell	<p>Take two dumbbells and sit on a decline bench, the feet are firmly on the floor, the head is resting the bench. Hold the weights next to the chest, at the height of your nipples and press them up till the arms are stretched. Let the weight slowly and controlled down.</p>	7	/static/images/default-pic.png	101	5	3	9
72	Deficit Deadlift	<p>Preparation</p>\n<p>Stand on weight plate, bumper plate, or shallow elevated platform with loaded bar above feet. Squat down and grasp bar with shoulder width or slightly wider overhand or mixed grip.</p>\n<p> </p>\n<p>Execution</p>\n<p>Lift bar by extending hips and knees to full extension. Pull shoulders back at top of lift if rounded. Return weights to floor by bending hips back while allowing knees to bend forward, keeping back straight and knees pointed same direction as feet. Repeat.</p>\n<p> </p>\n<p>Comments</p>\n<p>Throughout lift, keep hips low, shoulders high, arms and back straight. Knees should point same direction as feet throughout movement. Keep bar close to body to improve mechanical leverage. Grip strength and strength endurance often limit ability to perform multiple reps at heavy resistances. Gym chalk, wrist straps, grip work, and mixed grip can be used to enhance grip. Mixed grip indicates one hand holding with overhand grip and other hand holding with underhand grip. Lever barbell jack can be used to lift barbell from floor for easier loading and unloading of weight plates.</p>\n<p>Barbell Deficit Deadlift emphasizes building strength through lowest portion of Deadlift. Target muscle is exercised isometrically. Heavy barbell deadlifts significantly engages Latissmus Dorsi. See Barbell Deficit Deadlift under Gluteus Maximus. Also see Deadlift Analysis.</p>	7	/static/images/default-pic.png	381	3	1	1
78	Dumbbell Goblet Squat	<p>Grasp dumbbell with both hands at the sides of the upper plates. Hold dumbbell in front of chest, close to torso. Place feet about shoulderwide apart, keep knees slightly bent.</p>\n<p>Squat down until thighs are parallel to floor. Keep back straight, bend and move hips backward to keep knees above feet. Return, keep knees slightly flexed. Repeat.</p>\n<p>Keep bodyweight on heels and look ahead or slightly above to keep back straight.</p>	7	/static/images/default-pic.png	300	6	3	10
84	Extenseurs - Face	<p>En face</p>\n<ol>\n<li>Tirer</li>\n<li>relacher doucement</li>\n</ol>	7	/static/images/default-pic.png	414	5	1	1
86	Flutter Kicks	<p>-Laying on the back, lift your straightened legs from the ground at a 45 degree angle. </p>\n<p>-As your Left foot travels downward and nearly touches the floor, your Right foot should seek to reach a 90 degree angle, or as close to one as possible.</p>\n<p>-Bring your R foot down until it nearly touches the floor, and bring your L foot upwards.  Maintain leg rigidity throughout the exercise.  Your head should stay off the ground, supported by tightened upper abdominals.</p>\n<p>-(L up R down, L down R up, x2)  ^v, v^, ^v, v^ = 1 rep</p>\n<p>-Primarily works the Rectus Abdominus, the hip flexors and the lower back. Secondarily works the Obliques.  Emphasis placed on the lower quadrant of the abs.</p>\n<p> </p>	7	/static/images/default-pic.png	303	1	1	8
90	French Press (skullcrusher) Dumbbells	<p>Hold the dumbbells and lay down on a flat bench in such a way that around 1/4 of your head is over the edge. Stretch your arms with the weights and bend them so that the dumbbells are lowered (make sure they don't touch each other). Just before they touch your forehead, push them up.</p>\n<p>Pay attention to your elbows and arms: only the triceps are doing the work, the rest of the arms should not move.</p>	7	/static/images/default-pic.png	85	2	2	15
92	Front Raises	<p>To execute the exercise, the lifter stands with their feet shoulder width apart and weights or resistance handles held by their side with a pronated (overhand) grip.</p>\n<p>The movement is to bring the arms up in front of the body to eye level and with only a slight bend in the elbow. This isolates the anterior deltoid muscle (front of the shoulder) and uses the anterior deltoid to lift the weight.</p>\n<p>When lifting it is important to keep the body still so the anterior deltoid is fully utilised; if the weight cannot be lifted by standing still then it is too heavy and a lower weight is needed. It is important to keep a slight bend in the elbow when lifting as keeping the elbow locked will add stress to the elbow joint and could cause injury.</p>\n<p>A neutral grip, similar to that used in the hammer curl, can also be used. With this variation the weight is again raised to eye level, but out to a 45 degree angle from the front of the body. This may be beneficial for those with shoulder injuries, particularly those related to the rotator cuff.</p>	7	/static/images/default-pic.png	233	7	1	1
98	Hammercurls on Cable	<p>Take a cable in your hands (palms parallel, point to each other), the body is straight. Bend the arms and bring the weight up with a fast movement. Without any pause bring it back down with a slow, controlled movement, but don't stretch completely your arms.</p>\n<p>Don't swing your body during the exercise, the biceps should do all the work here. The elbows are at your side and don't move.</p>	7	/static/images/default-pic.png	138	2	1	2
104	High Knees	<p>-Start with legs at a comfortable standing width</p>\n<p>-Run in place, bringing knees to or above waist level</p>	7	/static/images/default-pic.png	432	6	1	5
106	Hindu Squats	<p>Start with your feet shoulder width apart and arms slightly behind your back.</p>\n<p>As you descend towards the floor, raise your heels off the ground, while keeping your back as vertical  as possible. </p>\n<p>Upon attaining the bottom position, touch the hands to the heels.</p>\n<p>Then stand up ending with the heels on the ground, arms extended in front of the chest then rowing into the start position.</p>	7	/static/images/default-pic.png	650	6	1	10
110	Hyperextensions	<p>Lay on the hyperextension pad with the belly button just at the leading edge, the upper body can hang freely. Tense your whole back's muscles and bring your upper body up till it is horizontal, but not more. Go slowly down and don't relax your muscles.</p>	7	/static/images/default-pic.png	128	3	1	14
112	Incline Dumbbell Flye	<p>Use inclined bench. Hold dumbbells straight out to your sides, elbows slightly bent. Bring arms together above you, keeping angle of elbows fixed.</p>	7	/static/images/default-pic.png	206	5	3	9
118	Jogging	<p>Get your shoes on, go outside and start running at a moderate pace.</p>	7	/static/images/default-pic.png	423	6	1	1
124	Lat Pull Down (Leaning Back)	<p>Lean Back, Pull into chest</p>	7	/static/images/default-pic.png	188	3	1	7
88	Fly With Dumbbells	<p>Take two dumbbells and lay on a bench, make sure the feet are firmly on the ground and your back is not arched, but has good contact with the bench. The arms are stretched in front of you, about shoulder wide. Bend now the arms a bit and let them down with a half-circle movement to the side. Without changing the angle of the elbow bring them in a fluid movement back up.</p>	7	/static/images/default-pic.png	145	5	3	9
94	Full Sit Outs	<p>(A) Get in high plank position on your hands and toes.(B) Shift your weight to your left hand as you turn your body to the right; bend your right leg behind you and extend your right arm up. Return to the center and repeat on the opposite side. Continue, alternating sides.<strong>Make it easier:</strong> Don’t raise your arm after you bend your leg behind you.<strong>Make it harder:</strong> Balance with your arm and leg extended for two counts.</p>	7	/static/images/default-pic.png	326	1	7	6
96	Good Mornings		7	/static/images/default-pic.png	116	6	1	3
100	Handstand Pushup	The handstand push-up (press-up) - also called the vertical push-up (press-up) or the inverted push-up (press-up) also called commandos- is a type of push-up exercise where the body is positioned in a handstand. For a true handstand, the exercise is performed free-standing, held in the air. To prepare the strength until one has built adequate balance, the feet are often placed against a wall, held by a partner, or secured in some other way from falling. Handstand pushups require significant strength, as well as balance and control if performed free-standing.	7	/static/images/default-pic.png	807	7	7	14
102	Hercules Pillars	<p>Grab two cables stand in the middle so both have tension and hold</p>	7	/static/images/default-pic.png	291	2	1	2
108	Hip Thrust	<p>The bar should go directly on your upper thigh, directly below your crotch. Your feet should be directly under your knees. Push your hips up so that you form a straight line from your knees to your shoulders. Use a pad for comfort.</p>	7	/static/images/default-pic.png	854	6	1	6
114	Incline Dumbbell Row	<ol>\n<li>Using a neutral grip, lean into an incline bench.</li>\n<li>Take a dumbbell in each hand with a neutral grip, beginning with the arms straight. This will be your starting position.</li>\n<li>Retract the shoulder blades and flex the elbows to row the dumbbells to your side.</li>\n<li>Pause at the top of the motion, and then return to the starting position.</li>\n</ol>	7	/static/images/default-pic.png	340	3	2	1
116	Incline Pushups	<p>Regular push with a 30 degree incline.</p>	7	/static/images/default-pic.png	168	5	1	9
120	Kettlebell Swings	<p>Hold the kettlebell securely in both hands. Keep your back flat throughout the move, avoiding any rounding of the spine.Keeping your knees "soft", hinge your hips backwards, letting the kettlebell swing between your knees.</p>\n<p>You want to bend from the hips as far as you can <em>without letting your back round forwards</em>. Then, snap your hips forwards quickly and standing up straight, locking your body in an upright posture.</p>\n<p>The speed you do this will cause your arms and the kettlebell to swing up in front of you. Don't try to <em>lift</em> the kettlebell with your arms. The snapping forwards of your hips will cause the kettlebell to swing forwards through momentum. Depending on the weight of the kettlebell and the speed of your hip movement, your arms will swing up to about shoulder height. At the top of this swing, let your hips hinge backwards again as the kettlebell swings back down to between your legs and the start of the next repetition.</p>	7	/static/images/default-pic.png	249	6	1	6
122	Lateral Raises on Cable, One Armed	<p>.</p>	7	/static/images/default-pic.png	149	7	1	1
128	Leg Curls (sitting)		7	/static/images/default-pic.png	117	6	1	3
89	Fly With Dumbbells, Decline Bench	<p>The exercise is the same as with a regular bench:</p>\n<p>Take two dumbbells and lay on a bench, make sure the feet are firmly on the ground and your back is not arched, but has good contact with the bench. The arms are stretched in front of you, about shoulder wide. Bend now the arms a bit and let them down with a half-circle movement to the side. Without changing the angle of the elbow bring them in a fluid movement back up.</p>	7	/static/images/default-pic.png	146	5	3	9
91	French Press (skullcrusher) SZ-bar	<p>Hold the SZ-bar and lay down on a flat bench in such a way that around 1/4 of your head is over the edge. Stretch your arms with the bar and bend them so that the bar is lowered. Just before it touches your forehead, push it up.</p>\n<p>Pay attention to your elbows and arms: only the triceps are doing the work, the rest of the arms should not move.</p>	7	/static/images/default-pic.png	84	2	2	15
95	Glute Bridge	<p>Lie on you back with your hips and knees flexed, feet on the ground. From this position, raise your butt off of the ground to a height where your body makes a straight line from your knees to your shoulders. To make the exercise more intense, you can add weight by letting a barbell rest on your hips as you complete the motion, or you can put your feet on a slightly higher surface such as a step or a bench.</p>	7	/static/images/default-pic.png	408	6	1	6
97	Hammercurls	<p>Hold two dumbbells and sit on a bench with a straight back, the shoulders are slightly rolled backwards. Your pals point to your body. Bend the arms and bring the weight up with a fast movement. Don't rotate your hands, as with the curls. Without any pause bring the dumbbell down with a slow, controlled movement.</p>\n<p>Don't swing your body during the exercise, the biceps should do all the work here. The elbows are at your side and don't move.</p>	7	/static/images/default-pic.png	86	2	3	2
103	High Knee Jumps	<p>-Start with legs slightly wider than shoulder width</p>\n<p>-Drop into a bodyweight squat</p>\n<p>-As you hit the bottom of the squat, explode upwards into a jump while simultaneously tucking your knees into your chest midflight.  Remain tucked until the apex of your jump.</p>\n<p>-Land on both feet, making sure your knees are not locked so as to avoid excessive strain upon your joints.  Collect yourself into the next rep as quickly but under control as possible.</p>	7	/static/images/default-pic.png	304	6	1	3
109	Hollow Hold	<p>Get on a mat and lie on your back. Contract your abs, stretch your raise and legs and raise them (your head and shoulders are also be raised). Make sure your lower back remains in contact with the mat.</p>	7	/static/images/default-pic.png	383	1	4	8
111	Incline Bench Press	<p>To do slowly, tempo is 4010</p>	7	/static/images/default-pic.png	163	5	1	9
115	Incline Plank With Alternate Floor Touch	<p>Perform the plank with legs elevated, feet on a gymball. Once stabilised, slowly move one foot sideways off the ball, then make it touch the floor, then come back to starting position. Alternate with the other foot.</p>\n<p>This is a core exercise.</p>	7	/static/images/default-pic.png	165	1	1	11
117	Isometric Wipers	<p>Assume push-up position, with hands slightly wider than shoulder width.</p>\n<p>Shift body weight as far as possible to one side, allowing the elbow on that side to flex. </p>\n<p>Reverse the motion, moving completely over to the other side.</p>\n<p>Return to the starting position, and repeat for the desired number of repetitions.</p>	7	/static/images/default-pic.png	338	5	7	9
123	Lateral-to-Front Raises	<p>-(1) Perform a lateral raise, pausing at the top of the lift (2).</p>\n<p>-Instead of lowering the weight, bring it to the front of your body so that you appear to be at the top position of a front raise.  You will do this by using a Pec Fly motion, maintaining straight arms. (3)</p>\n<p>-Now lower the weight to your quadriceps, or, in other words, lower the dumbbells as though you are completing a Front Raise repetition. (4)</p>\n<p>-Reverse the motion:  Perform a front raise (5), at the apex of the lift use a Reverse Fly motion to position the weights at the top of a Lateral Raise (6), and finally, lower the weights until your palms are essentially touching the sides of your thighs (7).  THIS IS ONE REP.</p>\n<p>(1) l  <em>front view  </em>(2) -l- <em> FV  </em>  (3) l-  <em>side view</em>   (4) l  <em>SV/FV</em>   (5) l-  <em>SV  </em> (6) -l-  <em>FV  </em>  (7)  l  <em>FV/SV</em></p>	7	/static/images/default-pic.png	306	7	3	1
129	Leg Curls (standing)		7	/static/images/default-pic.png	118	6	1	3
99	Hand Grip	<p>chrome Hand Flex Grip to build up forearms muscles</p>	7	/static/images/default-pic.png	317	2	1	1
101	Hanging Leg Raises	<p>Hanging from bar or straps, bring legs up with knees extended or flexed</p>	7	/static/images/default-pic.png	166	1	1	11
105	High Pull	<p>Use a light barbell, perform explosive lift up starting from underneath knee cap level. Lift/raise explosively using hips, at shoulder level. Tempo: 2111</p>	7	/static/images/default-pic.png	164	7	1	1
107	Hip Raise, Lying	Lying down on your back, with your feet flat on the floor. Raise your hips up evenly as high as you can and hold for as long as you can.	7	/static/images/default-pic.png	376	3	7	3
113	Incline Dumbbell Press	<ul>\n<li>Bench should be angled anywhere from 30 to 45 degrees</li>\n<li>Be sure to press dumbbells straight upward (perpendicular to the floor)</li>\n</ul>	7	/static/images/default-pic.png	210	5	3	9
119	Jumping Jacks	<p>A jumping jack or star jump, also called side-straddle hop in the US military, is a physical jumping exercise performed by jumping to a position with the legs spread wide and the hands going overhead, sometimes in a clap, and then returning to a position with the feet together and the arms at the sides</p>	7	/static/images/default-pic.png	810	6	1	10
121	Lateral Raises	<p>.</p>	7	/static/images/default-pic.png	148	7	3	1
125	Lat Pull Down (Straight Back)	<p>Pull bar down to strenum and keep straight back.</p>	7	/static/images/default-pic.png	187	3	1	7
127	Leg Curls (laying)	<p>Lay on a bench and put your calves behind the leg holder (better if they are hold on around the lower calves). Hold a grip on the bars to make sure the body is firmly in place. Bend your legs bringing the weight up, go slowly back. During the exercise the body should not move, all work is done by the legs.</p>	7	/static/images/default-pic.png	154	6	1	3
126	Leg Curl	The leg curl, also known as the hamstring curl, is an isolation exercise that targets the hamstring muscles. The exercise involves flexing the lower leg against resistance towards the buttocks. Other exercises that can be used to strengthen the hamstrings are the glute-ham raise and the deadlift.	7	/static/images/default-pic.png	792	6	1	3
130	Leg Extension	The leg extension is a resistance weight training exercise that targets the quadriceps muscle in the legs. The exercise is done using a machine called the Leg Extension Machine. There are various manufacturers of these machines and each one is slightly different. Most gym and weight rooms will have the machine in their facility. The leg extension is an isolated exercise targeting one specific muscle group, the quadriceps. It should not be considered as a total leg workout, such as the squat or deadlift. The exercise consists of bending the leg at the knee and extending the legs, then lowering them back to the original position.	7	/static/images/default-pic.png	796	6	1	10
131	Leg Extension	The leg extension is a resistance weight training exercise that targets the quadriceps muscle in the legs. The exercise is done using a machine called the Leg Extension Machine. There are various manufacturers of these machines and each one is slightly different. Most gym and weight rooms will have the machine in their facility. The leg extension is an isolated exercise targeting one specific muscle group, the quadriceps. It should not be considered as a total leg workout, such as the squat or deadlift. The exercise consists of bending the leg at the knee and extending the legs, then lowering them back to the original position.	7	/static/images/default-pic.png	796	6	1	10
132	Leg Extension	The leg extension is a resistance weight training exercise that targets the quadriceps muscle in the legs. The exercise is done using a machine called the Leg Extension Machine. There are various manufacturers of these machines and each one is slightly different. Most gym and weight rooms will have the machine in their facility. The leg extension is an isolated exercise targeting one specific muscle group, the quadriceps. It should not be considered as a total leg workout, such as the squat or deadlift. The exercise consists of bending the leg at the knee and extending the legs, then lowering them back to the original position.	7	/static/images/default-pic.png	804	6	1	10
133	Leg Press	The leg press is a weight training exercise in which the individual pushes a weight or resistance away from them using their legs.	7	/static/images/default-pic.png	788	6	1	3
134	Leg Presses (narrow)	<p>The exercise is very similar to the wide leg press:</p>\n<p>Sit on the machine and put your feet on the platform so far apart  that you could just put another foot in between them. The feet are parallel and point up.</p>\n<p>Lower the weight so much, that the knees form a right angle. Push immediately the platform up again, without any pause. When in the lower position, the knees point a bit outwards and the movement should be always fluid.</p>	7	/static/images/default-pic.png	115	6	1	10
135	Leg Presses (wide)	<p>Sit on the machine and put your feet on the platform, a bit more than shoulder wide. The feet are turned outwards by a few degrees.</p>\n<p>Lower the weight so much, that the knees form a right angle. Push immediately the platform up again, without any pause. When in the lower position, the knees point a bit outwards and the movement should be always fluid.</p>	7	/static/images/default-pic.png	114	6	1	10
136	Leg Press on Hackenschmidt Machine		7	/static/images/default-pic.png	130	6	1	10
137	Leg Raise	The leg raise is a strength training exercise which targets the iliopsoas (the anterior hip flexors). Because the abdominal muscles are used isometrically to stabilize the body during the motion, leg raises are also often used to strengthen the rectus abdominis muscle and the internal and external oblique muscles.	7	/static/images/default-pic.png	791	6	1	8
138	Leg Raises, Lying	<p>Lay down on a bench and hold onto the recliner with your hands to keep you stable. Hold your legs straight and lift them till they make an angle of about 45°. Make a short pause of 1 sec. and go slowly down to the initial position. To increase the intensity you can make a longer pause of 7 sec. every 5th time.</p>	7	/static/images/default-pic.png	125	1	4	11
139	Leg Raises, Standing	<p>Put your forearms on the pads on the leg raise machine, the body is hanging freely. Lift now your legs with a fast movement as high as you can, make a short pause of 1sec at the top, and bring them down again. Make sure that during the exercise your body does not swing, only the legs should move.</p>	7	/static/images/default-pic.png	126	1	1	11
140	Leverage Machine Chest Press	<p>Be sure to adjust seat height so that the handles are towards the bottom of your pectorals.</p>	7	/static/images/default-pic.png	211	5	1	9
141	Leverage Machine Iso Row	<p>Adjust seat height so that the handles are at the bottom of your pectorals or just below.</p>	7	/static/images/default-pic.png	214	3	1	7
142	L Hold	<p>Hold the L position for as long as possible</p>	7	/static/images/default-pic.png	281	1	1	1
143	Long-Pulley (low Row)	<p>Sit down, put your feet on the supporting points and grab the bar with a wide grip. Pull the weight with a rapid movement towards your belly button, not upper. Keep your arms and elbows during the movement close to your body. Your shoulders are pulled together. Let the weight slowly down till your arms are completely stretched.</p>	7	/static/images/default-pic.png	143	3	1	7
144	Long-Pulley, Narrow	<p>The exercise is the same as the regular long pulley, but with a narrow grip:</p>\n<p>Sit down, put your feet on the supporting points and grab the bar with a wide grip. Pull the weight with a rapid movement towards your belly button, not upper. Keep your arms and elbows during the movement close to your body. Your shoulders are pulled together. Let the weight slowly down till your arms are completely stretched.</p>	7	/static/images/default-pic.png	144	3	1	7
145	Low Box Squat - Wide Stance	<p>Unrack the bar and set your stance wide, beyond your hips.  Push your hips back and sit down to a box that takes you below parallel.  Sit completely down, do not touch and go.  Then explosively stand up.  Stay tight in your upper back and torso throughout the movement.</p>	7	/static/images/default-pic.png	389	6	1	6
146	Lying Rotator Cuff Exercise	<p>This is an excercise for problems with the levator muscles. Primary  Infraspinatus, secondary Teres Minor.</p>\n<p>Lying on side. Keep elbow on waist and in 90 dgr angle. Rotate towards stomach. Add weight as fit.</p>	7	/static/images/default-pic.png	312	7	3	1
147	MGM Machine		7	/static/images/default-pic.png	141	3	1	7
153	Overhead Squat	<p>The barbell is held overhead in a wide-arm snatch grip; however, it is also possible to use a closer grip if balance allows.</p>	7	/static/images/default-pic.png	355	6	1	1
148	Military Press	<p>The military press is a variation of the overhead press weight training exercise using very strict form and no pre-movement momentum.The military press targets the deltoid muscles in the shoulders as well as the triceps. Additionally, it works the core and legs, which the lifter uses to help stabilize the weight.The lift begins with the lifter standing and the barbell on the anterior deltoids. The lifter then raises the barbell overhead by pressing the palms of the hands against the underside of the barbell.</p>	7	/static/images/default-pic.png	229	7	1	1
154	Pause Bench	<p>Lower the bar to your chest and pause (but do not rest) there for 2 seconds. Press back up. use the same weight you would on bench press, but perform only single reps. Total the number of reps you did in one set of bench press (if you did 3 sets of 8 do 8 sinlge pause bench reps.</p>	7	/static/images/default-pic.png	270	5	1	9
156	Perfect Push Up	<p>Push up with perfect push up</p>	7	/static/images/default-pic.png	182	5	1	9
160	Power Clean	<p>Olympic weight lifting</p>	7	/static/images/default-pic.png	189	7	1	9
162	Prone Scapular Retraction - Arms at Side	<p>Lying on stomach with head on towel.</p>\n<p>Stretch arms straight out to your sides.</p>\n<p>Slowly lift your arms, pulling your shoulderblades together, hold for 3 seconds.</p>\n<p> </p>	7	/static/images/default-pic.png	429	3	1	14
168	Rack Deadlift	<p>Deadlift to be done using a Smith machine or a free rack. Bar or barbell hould be just right under the knee cap level. Lift using the glutes and through the heels, then come back to starting postion with a control movement of 2 seconds.</p>\n<p>This exercise targets mainly the lower back and glutes.</p>	7	/static/images/default-pic.png	161	3	1	6
174	Reverse Plank	<p>Plank with stomach towards ceiling</p>	7	/static/images/default-pic.png	409	1	1	1
176	Roman Chair	<p>Crunches on roman chair</p>	7	/static/images/default-pic.png	263	1	1	1
180	Rowing, Seated		7	/static/images/default-pic.png	108	3	1	7
182	Run	<p>Running or jogging outside in a park, on the tracks,...</p>	7	/static/images/default-pic.png	397	6	1	1
185	Scissors	<p>Scissors is an abdominal exercise that strengthens the transverse abdominals, helping flatten your belly and strengthen your entire core. Scissors is not only a core strength move, but it is also a great stretch for your hamstrings and your lower back. Everyone is looking for new ways to work the core, to flatten the belly and to improve flexibility. If you learn how to do Scissors you will get everything rolled together in one move.</p>	7	/static/images/default-pic.png	631	1	1	11
188	Run - Interval Training 	<p>Run and do some interval trainings such as hill repat, fartlek,..</p>	7	/static/images/default-pic.png	398	6	1	1
193	Shoulder Fly	The shoulder fly (also known as a lateral raise) works the deltoid muscle of the shoulder. The movement starts with the arms straight, and the hands holding weights at the sides or in front of the body. Body is in a slight forward-leaning position with hips and knees bent a little. Arms are kept straight or slightly bent, and raised through an arc of movement in the coronal plane that terminates when the hands are at approximately shoulder height. Weights are lowered to the starting position, completing one rep. When using a cable machine the individual stands with the coronal plane in line with the pulley, which is at or near the ground.[9] The exercise can be completed one shoulder at a time (with the other hand used to stabilize the body against the weight moved), or with both hands simultaneously if two parallel pulleys are available.	7	/static/images/default-pic.png	802	7	3	1
199	Shrugs, Barbells	<p>Take a barbell and stand with a straight body, the arms are hanging freely in front of you. Lift from this position the shoulders as high as you can, but don't bend the arms during the movement. On the highest point, make a short pause of 1 or 2 seconds before returning slowly to the initial position.</p>\n<p>When training with a higher weight, make sure that you still do the whole movement!</p>	7	/static/images/default-pic.png	150	7	1	1
201	Side Crunch	<p>Hold weight in one hand. Bend side ways to the knee. Pull upo to upright position using your obliquus.</p>	7	/static/images/default-pic.png	176	1	4	8
205	Side Raise	<p>Stand up or sit , keep both weights in front against legs or at side. Keep arms at around a 90 degree angle. Lift elbows up slowly and squeese traps when at topmost position. Lower the weights slowly back to starting position.</p>\n<p>2 seconds up, 2 seconds down</p>	7	/static/images/default-pic.png	319	7	1	1
207	Single-arm Preacher Curl	<p>Sit on the preacher curl bench and perform a bicep curl with a dumbbell in one hand. Your other hand can be at rest, or beneath your curling arm's elbow.</p>	7	/static/images/default-pic.png	205	2	3	2
213	Speed Deadlift	<p>Deadlift with short (&lt;1min) rest between sets.</p>	7	/static/images/default-pic.png	328	6	1	1
149	Military Press	<p>On an SZ-bar grip your hands on the outside of each bend and stand with your arms straight down, palms facing your legs. Pull the bar (bending your arms at the elbow) to your chest, and the push the bar above your head (arms as straight as possible). Return the bar to your chest by dropping your arms at the elbows. Return the bar to it's origional position (stand with your arms straight down, palms facing your legs.)</p>	7	/static/images/default-pic.png	256	2	10	1
151	Negative Crunches	<p>Sit yourself on the decline bench and fix your legs. Cross your arms over the chest and bring with a rolling movement your upper body up, go now without a pause and with a slow movement down again. Don't let your head move during the exercise.</p>	7	/static/images/default-pic.png	93	1	1	11
155	Pendelay Rows	<p>Back excercise with a barbell with a starting position which is in a bent over position with the back paralell to the ground. The barbell is on the ground at chest level.For the movement grab the barbell at shoulder width grip and pull towards your chest without losing the bent over position and without moving anything but your arms</p>	7	/static/images/default-pic.png	202	3	1	7
157	Pike Push Ups	<p>Push Up performed from a pike position (optional to have feet elevated).</p>	7	/static/images/default-pic.png	361	2	7	9
163	Pull-ups	<p>Grab the pull up bar with a wide grip, the body is hanging freely. Keep your chest out and pull yourself up till your chin reaches the bar or it touches your neck, if you want to pull behind you. Go with a slow and controlled movement down, always keeping the chest out.</p>	7	/static/images/default-pic.png	107	3	8	7
169	Rear Delt Raises	<p>Seated on a bench bWith the dumbbells on the floor bend over at 45 Degrees and then slowly raise each dumbbell to shoulder height and hold for a couple seconds before lowering to the starting position. </p>\n<p> </p>	7	/static/images/default-pic.png	237	7	3	1
171	Reverse Bar Curl	<p>Hold bar with reverse (or "overhand") grip, palms facing the floor.</p>	7	/static/images/default-pic.png	208	2	10	2
175	Ring Dips	<p>Dips peformed on gymnastic rings.</p>	7	/static/images/default-pic.png	360	2	1	15
177	Romanian Deadlift	<p>DL from top to pos 2: https://www.youtube.com/watch?v=WtWtjViRsKo</p>	7	/static/images/default-pic.png	351	6	1	1
183	Run - Interval Training 	<p>Run and do some interval trainings such as hill repat, fartlek,..</p>	7	/static/images/default-pic.png	398	6	1	1
189	Run - Treadmill	<p>Run on a treadmill</p>	7	/static/images/default-pic.png	269	6	1	1
194	Shoulder Press, Barbell	<p>Sit on a bench, the back rest should be almost vertical. Take a barbell with a shoulder wide grip and bring it up to chest height. Press the weight up, but don't stretch the arms completely. Go slowly down and repeat.</p>	7	/static/images/default-pic.png	119	7	1	1
196	Shoulder Press, on Machine		7	/static/images/default-pic.png	152	7	1	1
200	Shrugs, Dumbbells	<p>Stand with straight body, the hands are hanging freely on the side and hold each a dumbbell. Lift from this position the shoulders as high as you can, but don't bend the arms during the movement. On the highest point, make a short pause of 1 or 2 seconds before returning slowly to the initial position.</p>\n<p>When training with a higher weight, make sure that you still do the whole movement!</p>	7	/static/images/default-pic.png	151	7	3	1
202	Side Dumbbell Trunk Flexion	<p>AKA dumbbell side bends. Stand in line with the hips with slightly bent knees, maintain the natural curvature of the spine, hand stretched by the body, grip the barbell with one hand. <em> </em>Make slow and controlled torso side flexions till you reach the angle of approximately 45°.</p>	7	/static/images/default-pic.png	278	3	3	8
208	Sitting Calf Raises	<p>Sit on a bench for calf raises and check that the feet are half free and that you can completely stretch the calf muscles down. Pull your calves up, going as far (up) as you can. Make at the highest point a short pause of 1 or 2 seconds and go down.</p>	7	/static/images/default-pic.png	103	4	1	13
214	Splinter Sit-ups	<p>Lie on your back with your legs straight and arms at your sides, keeping your elbows bent at 90 degrees. As you sit up, twist your upper body to the left and bring your left knee toward your right elbow while you swing your left arm back. Lower your body to the starting position, and repeat to your right. That's 1 rep.</p>	7	/static/images/default-pic.png	170	1	1	8
150	Muscle up	<p>The body is then explosively pulled up by the arms in a radial pull-up, with greater speed than a regular pull-up. When the bar approaches the upper chest, the wrists are swiftly flexed to bring the forearms above the bar. The body is leaned forward, and the elbows are straightened by activating the triceps. The routine is considered complete when the bar is at the level of the waist and the arms are fully straight.</p>\n<p>To dismount, the arms are bent at the elbow, and the body is lowered to the floor, and the exercise can be repeated.</p>\n<p>As a relatively advanced exercise, muscle-ups are typically first learned with an assistive kip. The legs swing (kip) up and provide momentum to assist in the explosive upward force needed to ascend above the bar. More advanced athletes can perform a strict variation of the muscle-up which is done slowly, without any kip. This variation begins with a still dead hang and uses isometric muscle contraction to ascend above the bar in a slow, controlled fashion.</p>	7	/static/images/default-pic.png	626	3	8	2
152	Overhand Cable Curl	<p>Hands at shoulder height, curl arms in toward head, then back out.</p>	7	/static/images/default-pic.png	197	1	1	2
158	Pistol Squat	<p>One legged squat</p>	7	/static/images/default-pic.png	160	6	1	3
164	Pull Ups on Machine		7	/static/images/default-pic.png	140	3	1	7
166	Pushups	A push-up (or press-up if the hands are wider than shoulders placing more emphasis on the pectoral muscles) is a common calisthenics exercise beginning from the prone position. By raising and lowering the body using the arms, push-ups exercise the pectoral muscles, triceps, and anterior deltoids, with ancillary benefits to the rest of the deltoids, serratus anterior, coracobrachialis and the midsection as a whole. Push-ups are a basic exercise used in civilian athletic training or physical education and commonly in military physical training. They are also a common form of punishment used in the military, school sport, or some martial arts disciplines.	7	/static/images/default-pic.png	790	5	7	1
170	Renegade Row	<p>Get into pushup position gripping some dumbbells. Perform one pushup, then drive your left elbo up, bringing the dumbell up to your body. Return the dumbell to starting position. </p>\n<p>Perform another pushup and then row with the other arm to complete one rep.</p>	7	/static/images/default-pic.png	670	3	3	7
172	Reverse Curl	The reverse-grip barbell curl is a variation on the biceps curl where the palms face downward. The switch from an underhand to an overhand grip brings the forearm and brachialis muscles more into the exercise.	7	/static/images/default-pic.png	771	2	1	2
178	Row	In strength training, rowing (or a row, usually preceded by a qualifying adjective — for instance a seated row) is an exercise where the purpose is to strengthen the muscles that draw the rower's arms toward the body (latissimus dorsi) as well as those that retract the scapulae (trapezius and rhomboids) and those that support the spine (erector spinae). When done on a rowing machine, rowing also exercises muscles that extend and support the legs (quadriceps and thigh muscles). In all cases, the abdominal and lower back muscles must be used in order to support the body and prevent back injury.	7	/static/images/default-pic.png	801	3	1	7
181	Rowing, T-bar	<p>The execution of this exercise is very similar to the regular bent over rowing, only that the bar is fixed here.</p>\n<p>Grab the barbell with a wide grip (slightly more than shoulder wide) and lean forward. Your upper body is not quite parallel to the floor, but forms a slight angle. The chest's out during the whole exercise. Pull now the barbell with a fast movement towards your belly button, not further up. Go slowly down to the initial position. Don't swing with your body and keep your arms next to your body.</p>	7	/static/images/default-pic.png	106	3	1	7
184	Run - Treadmill	<p>Run on a treadmill</p>	7	/static/images/default-pic.png	269	6	1	1
187	Run	<p>Running or jogging outside in a park, on the tracks,...</p>	7	/static/images/default-pic.png	397	6	1	1
192	Shotgun Row	<ol>\n<li>Attach a single handle to a low cable.</li>\n<li>After selecting the correct weight, stand a couple feet back with a wide-split stance. Your arm should be extended and your shoulder forward. This will be your starting position.</li>\n<li>Perform the movement by retracting the shoulder and flexing the elbow. As you pull, supinate the wrist, turning the palm upward as you go.</li>\n<li>After a brief pause, return to the starting position.</li>\n</ol>	7	/static/images/default-pic.png	339	3	1	7
198	Shoulder Shrug	The shoulder shrug (usually called simply the shrug) is an exercise in weight training used to develop the upper trapezius muscle. The lifter stands erect, hands about shoulder width apart, and raises the shoulders as high as possible, and then lowers them, while not bending the elbows, or moving the body at all. The lifter may not have as large a range of motion as in a normal shrug done for active flexibility. It is usually considered good form if the slope of the shoulders is horizontal in the elevated position.	7	/static/images/default-pic.png	805	7	1	14
204	Side Plank	<p>Works your obliques and helps stabilize your spine. Lie on your side and support your body between your forearm and knee to your feet.</p>	7	/static/images/default-pic.png	325	1	7	11
206	Side to Side Push Ups	<p>-start in push up position</p>\n<p>-lean the body weight to the right side, and complete a push up with the chest over the right hand</p>\n<p>-come back to the centered position</p>\n<p>-on rep 2, lean to the left side</p>	7	/static/images/default-pic.png	302	5	1	1
210	Skipping - Standard	<p>Do a single, double footed jump for each swing of the rope.</p>\n<p>Work on a smooth, rhythmical movement, bouncing lightly on the balls of your feet.</p>	7	/static/images/default-pic.png	411	4	1	5
212	Snach	<p>Stand with your feet at hip width and your shins against the bar. Grasp the bar at double shoulder width and, keeping your lower back flat, drive your heels into the floor to begin lifting the bar. When it's above your knees, explosively extend your hips and shrug your shoulders. Let the momentum carry the weight overhead.</p>	7	/static/images/default-pic.png	271	7	1	1
159	Plank	<p>Get into a position on the floor supporting your weight on your forearms and toes. Arms are bent and directly below the shoulder. </p>\n<p>Keep your body straight at all times and hold this position as long as possible. To increase difficulty an arm or leg can be raised while performing this exercise.  </p>	7	/static/images/default-pic.png	238	1	7	8
161	Preacher Curls	<p> Place the EZ curl bar on the rest handles in front of the preacher bench. Lean over the bench and grab the EZ curl bar with palms up. Sit down on the preacher bench seat so your upper arms rest on top of the pad and your chest is pressed against the pad. Lower the weight until your elbows are extended and arms are straight. Bring the weights back up to the starting point by contracting biceps. Repeat</p>	7	/static/images/default-pic.png	193	2	1	4
165	Push Press	<p>olympic weight lifting</p>	7	/static/images/default-pic.png	190	7	1	14
167	Push Ups	<p>Start with your body streched, your hands are shoulder-wide appart on the ground. Push yourself off the ground till you strech your arms. The back is always straight and as well as the neck (always look to the ground). Lower yourself to the initial position and repeat.</p>	7	/static/images/default-pic.png	195	2	7	15
173	Reverse Grip Bench Press	<p>Upper chest focuses exercise that also works triceps</p>	7	/static/images/default-pic.png	399	5	1	9
179	Rowing, Lying on Bench		7	/static/images/default-pic.png	142	3	1	7
186	Rowing, T-bar	<p>The execution of this exercise is very similar to the regular bent over rowing, only that the bar is fixed here.</p>\n<p>Grab the barbell with a wide grip (slightly more than shoulder wide) and lean forward. Your upper body is not quite parallel to the floor, but forms a slight angle. The chest's out during the whole exercise. Pull now the barbell with a fast movement towards your belly button, not further up. Go slowly down to the initial position. Don't swing with your body and keep your arms next to your body.</p>	7	/static/images/default-pic.png	106	3	1	7
190	Scissors	<p>Scissors is an abdominal exercise that strengthens the transverse abdominals, helping flatten your belly and strengthen your entire core. Scissors is not only a core strength move, but it is also a great stretch for your hamstrings and your lower back. Everyone is looking for new ways to work the core, to flatten the belly and to improve flexibility. If you learn how to do Scissors you will get everything rolled together in one move.</p>	7	/static/images/default-pic.png	631	1	1	11
191	Seated Triceps Press	<p>Sit down on a back (better with back support). Take a dumbbell firmly with both hands and hold it with extended arms over your head. With your palms facing upward and holding the weight of the dumbbell, slowly lower the weight behind your head.</p>\n<p> </p>	7	/static/images/default-pic.png	386	2	2	15
195	Shoulder Press, Dumbbells	<p>Sit on a bench, the back rest should be almost vertical. Take two dumbbells and bring them up to shoulder height, the palms and the elbows point during the whole exercise to the front. Press the weights up, at the highest point they come very near but don't touch. Go slowly down and repeat.</p>	7	/static/images/default-pic.png	123	7	3	1
197	Shoulder Press, on Multi Press	<p>The exercise is basically the same as with a free barbell:</p>\n<p>Sit on a bench, the back rest should be almost vertical. Take a bar with a shoulder wide grip and bring it down to chest height. Press the weight up, but don't stretch the arms completely. Go slowly down and repeat.</p>	7	/static/images/default-pic.png	155	7	1	1
203	Side-lying External Rotation	<p>With a weight in one hand, lie on your side opposite the weight. Keep your knees slightly bent. Hold your elbow against your side, and extend your upper arm straight ahead of you. While continuing to hold your elbow against your side, rotate your upper arm 90 degrees upwards.</p>\n<p>It is helpful to place a towel under your armpit to help with the form on this exercise. Placing a support under your head for the duration of the exercise is also a good idea.</p>	7	/static/images/default-pic.png	422	7	1	1
209	Sit-ups	<p>Sit on a mat, your calves are resting on a bench, the knees make a right angle. Hold your hands behind your neck. Go now up with a rolling movement of your back, you should feel how the individual vertebrae lose contact with the mat. At the highest point, contract your abs as much as you can and hold there for 2 sec. Go now down, unrolling your back.</p>\n<p> </p>	7	/static/images/default-pic.png	95	1	1	11
211	Smith Machine Close-grip Bench Press	<p>Perform a standard bench press on the smith machine, but have your hands on the bar about shoulder width apart, and keep your elbows close to your body.</p>	7	/static/images/default-pic.png	218	2	1	15
215	Squat Jumps	<p>Jump wide, then close</p>	7	/static/images/default-pic.png	185	6	1	10
216	Squats	<p>Make sure you have put the barbell at a height where you can comfortably take it out and put it back in. Take it out and make yourself ready:</p>\n<ul>\n<li>The bar is somewhat lower than your shoulders</li>\n<li>The feet are quite apart and point out</li>\n<li>The head is in your neck and looks up</li>\n<li>The chest is out</li>\n</ul>\n<p>Go now slowly down, till your thighs are parallel with the floor, not lower. The knees point outwards, your butt, out. Make a small pause of 1 second and with as much energy as you can, push the weight up. Make a pause of 2 seconds and repeat.</p>	7	/static/images/default-pic.png	111	6	1	10
217	Squat Thrust	The burpee, or squat thrust, is a full body exercise used in strength training and as an aerobic exercise. The basic movement is performed in four steps and known as a four-count burpee: Begin in a standing position. Move into a squat position with your hands on the ground. (count 1) Kick your feet back into a plank position, while keeping your arms extended. (count 2) Immediately return your feet into squat position. (count 3) Stand up from the squat position (count 4)	7	/static/images/default-pic.png	795	6	7	6
218	Standing Bicep Curl	Stand holding dumbbells at shoulder width apart. Face forearm upward and keep upper arm still while raising each dumbbell up to your shoulder.	7	/static/images/default-pic.png	768	2	3	2
219	Standing Calf Raises	<p>Get onto the calf raises machine, you should able to completely push your calves down. Stand straight, don't make a hollow back and don't bend your legs. Pull yourself up as high as you can. Make a small pause of 1 - 2 seconds and go slowly down.</p>	7	/static/images/default-pic.png	102	4	1	5
221	Stationary Bike	<p>Ride a Stationary Bike with various tensions.</p>	7	/static/images/default-pic.png	293	6	1	1
223	Straight-arm Pull Down (bar Attachment)	<p>Use the straight bar attachment on a high pulley. Grasp the two ends of the bar with your palms facing downward and your arms straight out in front of you. Pull your hands down towards your hips, while keeping your arms straight, then raise them back up to the starting position.</p>	7	/static/images/default-pic.png	216	3	1	7
220	Standing Rope Forearm	<p>Grab a wrist roller tool with both hands while standing with your feet about shoulder width apart. If your gym does not have a wrist roller tool, you can easily put one together. All you need is a 5 or 10 pound weight plate, a strong thin rope about 3 feet long and a 6-8 inch stick or bar. Securely fasten the rope to the middle of the bar/stick and tie the other end of the rope to the weight plate. To begin this exercise, grab the bar/stick with both hands using an overhand grip. Extend both arms straight out in front of you, parallel to the floor. Next, roll the weight up from the floor by rapidly twisting the bar/stick with your hands and wrists. Once the weight reaches the top, slowly lower the plate back to the floor by reversing the motion of your hands and wrists. Repeat (if you can!).</p>	7	/static/images/default-pic.png	382	2	1	1
222	Stiff-legged Deadlifts	<ul>\n<li>Keep legs straight</li>\n<li>Keep back straight</li>\n</ul>	7	/static/images/default-pic.png	209	6	1	3
228	Thruster	<ol>\n<li>Start by doing a front squat</li>\n<li>At the top position, push the bar above your head (similar to a press)</li>\n<li>Lower the bar to the shoulders</li>\n</ol>	7	/static/images/default-pic.png	396	6	1	1
234	Triceps Machine	<p>.</p>	7	/static/images/default-pic.png	139	2	1	15
236	Turkish Get-Up	<p>Starting on back, move to the standing position with dumbbell in one hand.  Switch hands between reps.</p>	7	/static/images/default-pic.png	318	1	3	1
240	Upright Row, on Multi Press	<p>The movements are basically the same as with an SZ-bar, but you use the bar on the multi press:</p>\n<p>Stand straight, your feet are shoulder-width apart. Hold the bar with an overhand grip on your thighs, the arms are stretched. Lift the bar close to the body till your chin. The elbows point out so that at the highest point they form a V. Make here a short pause before going slowly down and repeating the movement.</p>	7	/static/images/default-pic.png	147	7	1	1
242	Upright Row w/ Dumbbells	<p>Feet apart at shoulder width. Nice and Slow!</p>	7	/static/images/default-pic.png	311	7	3	1
248	Weighted Step	<p>Box step-ups w/ barbell, 45's on each side</p>	7	/static/images/default-pic.png	320	6	1	1
224	Straight-arm Pull Down (rope Attachment)	<p>Use the rope attachment on a high pulley. Grasp the two ends of the rope with your arms straight out in front of you. Pull your hands down towards your hips, while keeping your arms straight, then raise them back up to the starting position.</p>	7	/static/images/default-pic.png	215	3	1	7
226	Sumo Squats	<p>Stand with your feet wider than your shoulders, with your toes pointed out at a 45 degree angle and barbell on your shoulder.</p>\n<p>While keeping your back straight, descend slowly by bending at the knees and hips as if you are sitting down (squatting).</p>\n<p>Lower yourself until your quadriceps and hamstrings are parallel to the floor.</p>\n<p>Return to the starting position by pressing upwards and extending your legs while maintaining an equal distribution of weight on your forefoot and heel.</p>	7	/static/images/default-pic.png	570	6	1	6
230	Triceps Bench Press One Barbell	<p>Činka v jedné ruce v úrovni ramene. Zvedat do výšky napnuté paže a zpět. Provádět pomalu.</p>	7	/static/images/default-pic.png	186	2	1	15
232	Triceps Extensions on Cable	<p>Grab the cable, stand with your feet shoulder wide, keep your back straight and lean forward a little. Push the bar down, making sure the elbows don't move during the exercise. Rotate your hands outwards at the very end and go back to the initial position without pause.</p>	7	/static/images/default-pic.png	89	2	1	15
238	Upper Body	<p>Full workout of the upper arms body n chest. Focusing on the core</p>	7	/static/images/default-pic.png	393	5	1	1
244	Wall Handstand	<p>Handstand against a wall for support (chest facing wall).</p>	7	/static/images/default-pic.png	359	7	7	1
246	Wall Slides	<p>Stand with heels,  shoulders, back of head,  and hips touching the wall. Start with biceps straight out and elbows at a 90 degree angle. Straighten the arms while remaining againstthe wall without arching the back off of the wall, mimicking a shoulder press movement. </p>	7	/static/images/default-pic.png	548	3	7	2
250	Wide-grip Pulldown	<p>Lat pulldowns with a wide grip on the bar.</p>	7	/static/images/default-pic.png	204	3	1	7
225	Sumo Deadlift	<ol>\n<li>Begin with a bar loaded on the ground. Approach the bar so that the bar intersects the middle of the feet. The feet should be set very wide, near the collars. Bend at the hips to grip the bar. The arms should be directly below the shoulders, inside the legs, and you can use a pronated grip, a mixed grip, or hook grip. Relax the shoulders, which in effect lengthens your arms.</li>\n<li>Take a breath, and then lower your hips, looking forward with your head with your chest up. Drive through the floor, spreading your feet apart, with your weight on the back half of your feet. Extend through the hips and knees.</li>\n<li>As the bar passes through the knees, lean back and drive the hips into the bar, pulling your shoulder blades together.</li>\n<li>Return the weight to the ground by bending at the hips and controlling the weight on the way down.</li>\n</ol>	7	/static/images/default-pic.png	557	6	1	10
227	Superman	<p>Lay flat on your stomach with your arms extended in front of you on the ground as your legs are lying flat. Lift both your arms and legs at the same time, as if you were flying, and contract the lower back. Make sure that you are breathing and, depending on your fitness level, hold the movement for at least two to five seconds per repetition.</p>	7	/static/images/default-pic.png	330	3	4	6
233	Triceps Extensions on Cable With Bar	<p>Grab the bar, stand with your feet shoulder wide, keep your back straight and lean forward a little. Push the bar down, making sure the elbows don't move during the exercise. Without pause go back to the initial position.</p>	7	/static/images/default-pic.png	90	2	1	15
239	Upper External Oblique	<p>Exercise for upper external oblique muscles</p>	7	/static/images/default-pic.png	258	5	8	8
241	Upright Row, SZ-bar	<p>Stand straight, your feet are shoulder-width apart. Hold the SZ-bar with an overhand grip on your thighs, the arms are stretched. Lift the bar close to the body till your chin. The elbows point out so that at the highest point they form a V. Make here a short pause before going slowly down and repeating the movement.</p>	7	/static/images/default-pic.png	127	7	10	1
245	Wall Pushup	<p>Pushup against a wall</p>	7	/static/images/default-pic.png	203	2	7	1
247	Wall Squat	<p>Find a nice flat piece of wall and stand with your back leaning against the wall. Slowly slide down the wall while moving your feet away from it, until your thighs are parallel to the ground and both your knees and your hips are bent at a 90° angle. Cross your arms in front of your chest and hold this position for 30 seconds.</p>\n<p>Variant: put a big inflated rubber ball (like a small basketball) between your knees and squeeze the ball while holding the squat position</p>	7	/static/images/default-pic.png	387	6	7	3
229	Tricep Dumbbell Kickback	<ol>\n<li>Start with a dumbbell in each hand and your palms facing your torso. Keep your back straight with a slight bend in the knees and bend forward at the waist. Your torso should be almost parallel to the floor. Make sure to keep your head up. Your upper arms should be close to your torso and parallel to the floor. Your forearms should be pointed towards the floor as you hold the weights. There should be a 90-degree angle formed between your forearm and upper arm. This is your starting position.</li>\n<li>Now, while keeping your upper arms stationary, exhale and use your triceps to lift the weights until the arm is fully extended. Focus on moving the forearm.</li>\n<li>After a brief pause at the top contraction, inhale and slowly lower the dumbbells back down to the starting position.</li>\n<li>Repeat the movement for the prescribed amount of repetitions.</li>\n</ol>\n<p><strong>Variations:</strong> This exercise can be executed also one arm at a time much like the one arm rows are performed.</p>\n<p>Also, if you like the one arm variety, you can use a low pulley handle instead of a dumbbell for better peak contraction. In this case, the palms should be facing up (supinated grip) as opposed to the torso (neutral grip).</p>	7	/static/images/default-pic.png	279	2	3	15
231	Triceps Dips	<p>lift on parallel bars hold for 1 second, and lower slowly and control for 4 seconds, then come back with no rest (tempo: 4010)</p>	7	/static/images/default-pic.png	162	2	1	15
235	Trunk Rotation With Cable 	<p>Seated trunk rotation with cable </p>	7	/static/images/default-pic.png	310	1	1	8
237	Underhand Lat Pull Down	<p>Grip the pull-down bar with your palms facing you and your hands closer than shoulder-width apart. Lean back slightly and keep your back straight. Pull the bar down towards your chest, pulling your shoulders back slightly at the end of the motion.</p>	7	/static/images/default-pic.png	212	3	1	7
243	V-Bar Pulldown	<p>Pulldowns using close grip v-bar.</p>	7	/static/images/default-pic.png	424	3	1	1
249	Weighted Step-ups	<p>box step ups w/ barbell and 45's on each side</p>	7	/static/images/default-pic.png	321	6	1	1
251	Z Curls	<p>-Perform a traditional dumbbell biceps curl, pausing at the top of the motion.</p>\n<p>-Twist your hands until your palms are facing away from your shoulders (in reverse curl position).  Basically, twist your right wrist inwards to the left, and vice versa.</p>\n<p>-In a slow, controlled movement, lower the Dbells with your palms facing the ground.  At the bottom of the motion, twist your wrists back into the traditional curl grip (palms facing up, towards shoulder).</p>\n<p>-That is 1 rep</p>\n<p> </p>	7	/static/images/default-pic.png	305	2	1	2
\.


--
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.images (id, exercise_image_url, wger_id) FROM stdin;
1	https://wger.de/media/exercise-images/91/Crunches-1.png	91
2	https://wger.de/media/exercise-images/93/Decline-crunch-1.png	93
3	https://wger.de/media/exercise-images/128/Hyperextensions-1.png	128
4	https://wger.de/media/exercise-images/88/Narrow-grip-bench-press-1.png	88
5	https://wger.de/media/exercise-images/129/Standing-biceps-curl-1.png	129
6	https://wger.de/media/exercise-images/81/Biceps-curl-1.png	81
7	https://wger.de/media/exercise-images/74/Bicep-curls-1.png	74
8	https://wger.de/media/exercise-images/82/Tricep-dips-2-1.png	82
9	https://wger.de/media/exercise-images/83/Bench-dips-1.png	83
10	https://wger.de/media/exercise-images/151/Dumbbell-shrugs-2.png	151
11	https://wger.de/media/exercise-images/150/Barbell-shrugs-1.png	150
12	https://wger.de/media/exercise-images/86/Bicep-hammer-curl-1.png	86
13	https://wger.de/media/exercise-images/138/Hammer-curls-with-rope-1.png	138
14	https://wger.de/media/exercise-images/195/Push-ups-1.png	195
15	https://wger.de/media/exercise-images/84/Lying-close-grip-triceps-press-to-chin-1.png	84
16	https://wger.de/media/exercise-images/45/Seated-triceps-press-1.png	45
17	https://wger.de/media/exercise-images/116/Good-mornings-2.png	116
18	https://wger.de/media/exercise-images/192/Bench-press-1.png	192
19	https://wger.de/media/exercise-images/62/Barbell-upright-rows-2.png	62
20	https://wger.de/media/exercise-images/181/Chin-ups-2.png	181
21	https://wger.de/media/exercise-images/76/T-bar-row-1.png	76
22	https://wger.de/media/exercise-images/106/T-bar-row-1.png	106
23	https://wger.de/media/exercise-images/109/Barbell-rear-delt-row-1.png	109
24	https://wger.de/media/exercise-images/70/Reverse-grip-bent-over-rows-1.png	70
25	https://wger.de/media/exercise-images/110/Reverse-grip-bent-over-rows-1.png	110
26	https://wger.de/media/exercise-images/193/Preacher-curl-3-1.png	193
27	https://wger.de/media/exercise-images/11/Rear-deltoid-row-2.png	11
28	https://wger.de/media/exercise-images/16/Incline-press-1.png	16
29	https://wger.de/media/exercise-images/61/Close-grip-bench-press-1.png	61
30	https://wger.de/media/exercise-images/98/Butterfly-machine-2.png	98
31	https://wger.de/media/exercise-images/97/Dumbbell-bench-press-1.png	97
32	https://wger.de/media/exercise-images/100/Decline-bench-press-1.png	100
33	https://wger.de/media/exercise-images/163/Incline-bench-press-1.png	163
34	https://wger.de/media/exercise-images/122/Incline-cable-flyes-1.png	122
35	https://wger.de/media/exercise-images/113/Walking-lunges-1.png	113
36	https://wger.de/media/exercise-images/130/Narrow-stance-hack-squats-1-1024x721.png	130
37	https://wger.de/media/exercise-images/71/Cable-crossover-2.png	71
38	https://wger.de/media/exercise-images/41/Incline-bench-press-1.png	41
39	https://wger.de/media/exercise-images/56/Decline-crunch-1.png	56
40	https://wger.de/media/exercise-images/34/Leg-raises-2.png	34
41	https://wger.de/media/exercise-images/125/Leg-raises-2.png	125
42	https://wger.de/media/exercise-images/143/Cable-seated-rows-2.png	143
43	https://wger.de/media/exercise-images/161/Dead-lifts-2.png	161
44	https://wger.de/media/exercise-images/176/Cross-body-crunch-1.png	176
45	https://wger.de/media/exercise-images/191/Front-squat-1-857x1024.png	191
46	https://wger.de/media/exercise-images/111/Wide-stance-squat-2.gif	111
47	https://wger.de/media/exercise-images/39/Seated-leg-curl-1.png	39
48	https://wger.de/media/exercise-images/177/Seated-leg-curl-1.png	177
49	https://wger.de/media/exercise-images/119/seated-barbell-shoulder-press-large-1.png	119
50	https://wger.de/media/exercise-images/123/dumbbell-shoulder-press-large-1.png	123
51	https://wger.de/media/exercise-images/152/seated-shoulder-press-machine-large-1.png	152
52	https://wger.de/media/exercise-images/148/lateral-dumbbell-raises-large-2.png	148
53	https://wger.de/media/exercise-images/154/lying-leg-curl-machine-large-1.png	154
54	https://wger.de/media/exercise-images/117/seated-leg-curl-large-1.png	117
55	https://wger.de/media/exercise-images/118/standing-leg-curls-large-1.png	118
56	https://wger.de/media/exercise-images/231/Standing-biceps-curl-1.png	231
57	https://wger.de/media/exercise-images/53/Shoulder-press-machine-2.png	53
58	https://wger.de/media/exercise-images/244/Close-grip-front-lat-pull-down-2.png	244
59	https://wger.de/media/exercise-images/91/Crunches-1.png	91
60	https://wger.de/media/exercise-images/93/Decline-crunch-1.png	93
61	https://wger.de/media/exercise-images/128/Hyperextensions-1.png	128
62	https://wger.de/media/exercise-images/88/Narrow-grip-bench-press-1.png	88
63	https://wger.de/media/exercise-images/129/Standing-biceps-curl-1.png	129
64	https://wger.de/media/exercise-images/81/Biceps-curl-1.png	81
65	https://wger.de/media/exercise-images/74/Bicep-curls-1.png	74
66	https://wger.de/media/exercise-images/82/Tricep-dips-2-1.png	82
67	https://wger.de/media/exercise-images/83/Bench-dips-1.png	83
68	https://wger.de/media/exercise-images/151/Dumbbell-shrugs-2.png	151
69	https://wger.de/media/exercise-images/150/Barbell-shrugs-1.png	150
70	https://wger.de/media/exercise-images/86/Bicep-hammer-curl-1.png	86
71	https://wger.de/media/exercise-images/138/Hammer-curls-with-rope-1.png	138
72	https://wger.de/media/exercise-images/195/Push-ups-1.png	195
73	https://wger.de/media/exercise-images/84/Lying-close-grip-triceps-press-to-chin-1.png	84
74	https://wger.de/media/exercise-images/45/Seated-triceps-press-1.png	45
75	https://wger.de/media/exercise-images/116/Good-mornings-2.png	116
76	https://wger.de/media/exercise-images/192/Bench-press-1.png	192
77	https://wger.de/media/exercise-images/62/Barbell-upright-rows-2.png	62
78	https://wger.de/media/exercise-images/181/Chin-ups-2.png	181
\.


--
-- Data for Name: muscles; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.muscles (id, muscle_name, image_url) FROM stdin;
1	Anterior deltoid	/static/images/default-pic.png
2	Biceps brachii	/static/images/default-pic.png
3	Biceps femoris	/static/images/default-pic.png
4	Brachialis	/static/images/default-pic.png
5	Gastrocnemius	/static/images/default-pic.png
6	Gluteus maximus	/static/images/default-pic.png
7	Latissimus dorsi	/static/images/default-pic.png
8	Obliquus externus abdominis	/static/images/default-pic.png
9	Pectoralis major	/static/images/default-pic.png
10	Quadriceps femoris	/static/images/default-pic.png
11	Rectus abdominis	/static/images/default-pic.png
12	Serratus anterior	/static/images/default-pic.png
13	Soleus	/static/images/default-pic.png
14	Trapezius	/static/images/default-pic.png
15	Triceps brachii	/static/images/default-pic.png
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.teams (id, name, location, discipline, team_image_url, created_on, user_id) FROM stdin;
1	Volta	Las Vegas, NV, USA	acrobatics	/static/images/default-pic.png	2021-04-27 00:00:00	1
2	Fitness Coders	San Diego, NV, USA	brain gymnastics	/static/images/default-pic.png	2021-04-27 00:00:00	1
3	La Nouba	Orlando, FL, USA	acrobatics	/static/images/default-pic.png	2021-04-27 00:00:00	2
4	Seneca	Toronto, ONT, CAN	cycling	/static/images/default-pic.png	2021-04-27 00:00:00	2
5	ProRhytmics	Denver, CO, USA	Rhytmic Gymnastics	/static/images/default-pic.png	2021-04-27 00:00:00	3
6	AerialFusion	Austin, TX, USA	Aerial Arts	/static/images/default-pic.png	2021-04-27 00:00:00	3
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.users (id, username, password, email, first_name, last_name, image_url, header_image_url, created_on) FROM stdin;
1	edeneault	password1	edeneault@gmail.com	Etienne	Deneault	https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg	https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80	2021-04-27 00:00:00
2	msparks	password2	msparks@fakegmail.com	Matthew	Sparks	/static/images/default-pic.png	/static/images/warbler-hero.jpg	2021-04-27 00:00:00
3	adeneault	password3	apjarova@gmail.com	Alexandra	Deneault	https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg	https://images.unsplash.com/photo-1519925610903-381054cc2a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80	2021-04-27 00:00:00
4	beachcoach	BeachCoach	beach@coach.com	Laura	Summers	https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg	https://images.unsplash.com/photo-1519925610903-381054cc2a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80	2021-04-27 00:00:00
\.


--
-- Data for Name: workout_exercises; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.workout_exercises (id, workout_id, exercise_id) FROM stdin;
1	1	1
2	1	2
3	2	3
4	2	4
5	2	5
6	2	1
7	3	3
8	3	2
9	4	5
10	4	4
11	4	2
12	5	1
13	5	2
14	5	3
15	6	4
16	6	5
17	7	3
18	7	2
19	7	5
20	8	1
21	8	2
22	8	5
23	9	1
24	9	2
25	10	4
26	10	5
27	11	142
28	11	25
\.


--
-- Data for Name: workouts; Type: TABLE DATA; Schema: public; Owner: edeneault
--

COPY public.workouts (id, name, description) FROM stdin;
1	Upper Body Strength	Workout targets upperbody strength
2	Lower Body Strength	Workout targets lowerbody strength
3	Core Strength	Workout targets core strength
4	Lower Body Endurance	Tabata Style workout targets lowerbody endurance
5	Upper Body Endurance	Tabata Style workout targets lowerbody endurance
6	Core Body Endurance	Tabata Style workout targets lowerbody endurance
7	Total Body	EMOM style workout for Total Body strength and endurance
8	Hiit - hardcore	HiiT workout - a hardcore challenge
9	Hiit - medium	HiiT workout - a medium challenge
10	Hiit - starter	HiiT workout - a starter challenge
11	Test Workout 3	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
\.


--
-- Name: athlete_workouts_exercises_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.athlete_workouts_exercises_id_seq', 20, true);


--
-- Name: athlete_workouts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.athlete_workouts_id_seq', 20, true);


--
-- Name: athletes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.athletes_id_seq', 36, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.categories_id_seq', 7, true);


--
-- Name: equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.equipment_id_seq', 10, true);


--
-- Name: exercises_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.exercises_id_seq', 251, true);


--
-- Name: images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.images_id_seq', 78, true);


--
-- Name: muscles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.muscles_id_seq', 15, true);


--
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.teams_id_seq', 6, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- Name: workout_exercises_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.workout_exercises_id_seq', 28, true);


--
-- Name: workouts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edeneault
--

SELECT pg_catalog.setval('public.workouts_id_seq', 11, true);


--
-- Name: athlete_workouts_exercises athlete_workouts_exercises_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts_exercises
    ADD CONSTRAINT athlete_workouts_exercises_pkey PRIMARY KEY (id);


--
-- Name: athlete_workouts athlete_workouts_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts
    ADD CONSTRAINT athlete_workouts_pkey PRIMARY KEY (id);


--
-- Name: athletes athletes_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athletes
    ADD CONSTRAINT athletes_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: equipment equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT equipment_pkey PRIMARY KEY (id);


--
-- Name: exercises exercises_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_pkey PRIMARY KEY (id);


--
-- Name: images images_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);


--
-- Name: muscles muscles_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.muscles
    ADD CONSTRAINT muscles_pkey PRIMARY KEY (id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: workout_exercises workout_exercises_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workout_exercises
    ADD CONSTRAINT workout_exercises_pkey PRIMARY KEY (id);


--
-- Name: workouts workouts_pkey; Type: CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workouts
    ADD CONSTRAINT workouts_pkey PRIMARY KEY (id);


--
-- Name: athlete_workouts athlete_workouts_athlete_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts
    ADD CONSTRAINT athlete_workouts_athlete_id_fkey FOREIGN KEY (athlete_id) REFERENCES public.athletes(id) ON DELETE CASCADE;


--
-- Name: athlete_workouts_exercises athlete_workouts_exercises_athlete_workout_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts_exercises
    ADD CONSTRAINT athlete_workouts_exercises_athlete_workout_id_fkey FOREIGN KEY (athlete_workout_id) REFERENCES public.athlete_workouts(id) ON DELETE CASCADE;


--
-- Name: athlete_workouts_exercises athlete_workouts_exercises_workout_exercise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts_exercises
    ADD CONSTRAINT athlete_workouts_exercises_workout_exercise_id_fkey FOREIGN KEY (workout_exercise_id) REFERENCES public.workout_exercises(id) ON DELETE CASCADE;


--
-- Name: athlete_workouts athlete_workouts_workout_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athlete_workouts
    ADD CONSTRAINT athlete_workouts_workout_id_fkey FOREIGN KEY (workout_id) REFERENCES public.workouts(id) ON DELETE CASCADE;


--
-- Name: athletes athletes_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.athletes
    ADD CONSTRAINT athletes_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(id) ON DELETE CASCADE;


--
-- Name: exercises exercises_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- Name: exercises exercises_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: exercises exercises_muscle_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_muscle_id_fkey FOREIGN KEY (muscle_id) REFERENCES public.muscles(id);


--
-- Name: teams teams_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: workout_exercises workout_exercises_exercise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workout_exercises
    ADD CONSTRAINT workout_exercises_exercise_id_fkey FOREIGN KEY (exercise_id) REFERENCES public.exercises(id) ON DELETE CASCADE;


--
-- Name: workout_exercises workout_exercises_workout_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edeneault
--

ALTER TABLE ONLY public.workout_exercises
    ADD CONSTRAINT workout_exercises_workout_id_fkey FOREIGN KEY (workout_id) REFERENCES public.workouts(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

