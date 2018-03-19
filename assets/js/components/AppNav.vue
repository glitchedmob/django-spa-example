<template>
	<b-navbar toggleable="md" type="dark" variant="primary">
		<b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

		<b-navbar-brand :to="{ name: 'home' }">Django Message Board</b-navbar-brand>

		<b-collapse is-nav id="nav_collapse">

			<transition-group name="fade" tag="ul" class="ml-auto navbar-nav">
				<b-nav-item :to="{ name: 'all-posts' }"  key="all" class="nav-item">All Posts</b-nav-item>
				<b-nav-item :to="{ name: 'create-post' }" v-if="loggedIn" exact key="create" class="nav-item">Create Post</b-nav-item>
				<b-nav-item :to="{ name: 'login' }" v-if="!loggedIn" exact key="login" class="nav-item">Login</b-nav-item>
				<b-nav-item v-else-if="loggedIn" @click="logout" key="logout" class="nav-item">Logout</b-nav-item>
			</transition-group>

		</b-collapse>
	</b-navbar>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
export default {
	computed: {
		...mapState(['loggedIn'])
	},
	methods: {
		...mapMutations(['login', 'logout'])
	}
}
</script>

<style lang="scss" scoped>
	.nav-item {
		transition: all 1s;
	}

	.fade-enter, .fade-leave-to {
		opacity: 0;
		transform: translateY(50px);
	}

	.fade-leave-active {
		position: absolute;
	}
</style>
